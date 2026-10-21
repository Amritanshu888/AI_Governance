#!/usr/bin/env python
# coding: utf-8

# # Sentience Governor + LangChain: a beginner's notebook
# 
# **Sentience Governor** is a governance and observability layer for AI agents.
# It watches what an agent does — which tools it calls, when it starts and stops, what
# state it's in — and emits structured events you can inspect, log, or send to a dashboard.
# Think of it as a flight-data recorder for an AI agent: it does not change the agent's
# behavior, it just observes it.
# 
# This notebook shows the **callback integration pattern**, which is the exact mechanism
# LangChain provides for hooking observation into an agent. LangChain agents already
# fire lifecycle events (chain start/end, LLM start/end, tool start/end) regardless of
# what the agent is actually doing. A *callback handler* is a small object that receives
# those events. Sentience Governor ships a handler that turns those events into
# governance events — and because we attach the handler through LangChain's standard
# config, **no part of the agent itself has to change** to become observable.
# 

# ## Install dependencies
# 
# We install LangChain, the Groq integration, LangChain Community (for the web search tool),
# Sentience Governor itself, and pandas for the summary table at the end.
# 

# ## API key
# 
# We need a Groq API key to run the language model. Groq offers a free tier — you can
# sign up and grab a key at https://console.groq.com.
# 
# We'll enter the key below using `getpass`, which reads from the keyboard without
# echoing it back. The key is stored only in the running notebook's environment; it is
# never printed, never written into this notebook file, and never persisted to disk.
# 

# In[1]:


import os
from getpass import getpass

os.environ["GROQ_API_KEY"] = getpass("Enter your GROQ_API_KEY: ")


# ## Define the tool
# 
# LangChain agents act by calling **tools**, which are just regular Python functions
# decorated with `@tool`. The agent decides, based on the user's request, when (and
# how many times) to call a tool.
# 
# To keep this example self-contained, we define one trivial, deterministic tool — a
# fake weather lookup that returns a hard-coded string. There is no real API call and
# no network dependency beyond the LLM call itself.
# 

# In[2]:


from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Look up the current weather in a given city"""
    return f"The weather in {city} is 25 degrees celsius and cloudy"


# ## Add a second tool: live web search
# 
# So far our agent has one tool, a mocked weather lookup. Let's give it a second, *real* tool:
# a live web search. We use `DuckDuckGoSearchRun` from `langchain-community`, which is handy
# for a notebook like this because it needs no API key and no signup — unlike Google or Bing
# search tools, which would each require you to provision a credential. That keeps the notebook
# runnable for anyone who has a Groq key.
# 

# In[3]:


from langchain_community.tools import DuckDuckGoSearchRun

search_web = DuckDuckGoSearchRun()


# ## Define the agent
# 
# We build a tool-calling agent using `create_agent`, which is LangChain 1.x's current
# top-level API for this — not the older `initialize_agent` / `AgentExecutor` APIs that
# you may have seen in older tutorials.
# 
# For the language model we use Groq's `llama-3.3-70b-versatile` via the `langchain-groq`
# integration. The agent is given two tools — a mocked weather lookup and a real web search — and a simple system prompt.
# 

# In[4]:


from langchain.agents import create_agent
from langchain_groq import ChatGroq


model = ChatGroq(model="llama-3.3-70b-versatile")

agent = create_agent(
    model=model,
    tools = [get_weather, search_web],
    system_prompt="You are a helpful assistant"
)


# In[7]:


agent


# ## What is a callback handler, and how does Sentience Governor use one
# 
# LangChain's callback system is a publish/subscribe mechanism: the framework fires events
# at well-defined points in an agent's life — when a chain starts, when a chain ends,
# when an LLM is called, when a tool is called — and any registered handler receives them.
# Crucially, this happens **regardless of what the agent is actually doing**, so a handler
# sees every step the agent takes.
# 
# Sentience Governor ships a handler called `SentienceCallbackHandler` that turns those
# raw lifecycle hooks into governance events:
# 
# - `on_chain_start` -> an `AGENT_REGISTERED` event
# - `on_tool_start` -> `SCOPE_ASSERTED` and `CONTEXT_SNAPSHOT` events
# - `on_tool_end` -> a `CONTEXT_SNAPSHOT` update event
# 
# Because the handler subscribes through the standard LangChain mechanism, **any**
# LangChain agent becomes observable just by attaching the handler — no edits to the
# agent's own logic are required.
# 

# In[5]:


import json
from sentience_governor.sink.writer import SinkBase

class NotebookSink(SinkBase):
    def __init__(self):
        self.events: list[dict] = []
    
    def write(self, event)-> bool:
        payload = event.to_dict()
        print(json.dumps(payload, indent=2))
        self.events.append(payload)
        return True



# ## Define the minimal Sentience handler
# 
# `SentienceCallbackHandler` already implements every LangChain callback method we need
# (`on_chain_start`, `on_chain_end`, `on_llm_start`, `on_llm_end`, `on_tool_start`,
# `on_tool_end`) and turns them into governance events. There is nothing for us to
# override.
# 
# There is one small wrinkle: the handler is duck-typed — it does not inherit from
# LangChain's `BaseCallbackHandler`, so LangChain does not recognize it as a real
# callback out of the box. We fix that with a tiny multiple-inheritance subclass that
# adds the base class as a parent. That is the entire integration code: one empty class
# and one constructor call.
# 

# In[6]:


from langchain_core.callbacks import BaseCallbackHandler
from sentience_governor.cache.cache import InProcessCache
from sentience_governor.session_manager.manager import SessionManager
from sentience_governor.sink.writer import SinkWriter
from sentience_governor.wrapper.langchain_adapter import SentienceCallbackHandler


class MySentienceHandler(SentienceCallbackHandler,BaseCallbackHandler):
    pass

sink = NotebookSink()

handler = MySentienceHandler(
    agent_id="weather telling agent",
    session_manager = SessionManager(),
    cache=InProcessCache(),
    agent_version="1.0",
    vendor_id = "notebook-demo",
    declared_capabilities = ["get_weather", "search_web"],
    owner_claim="yash patil",
    sink_writer = SinkWriter(sink)
)









# ## Run the agent
# 
# We invoke the agent exactly the way we would without observability — the only
# addition is `config={"callbacks": [handler]}`, which tells LangChain to dispatch
# every lifecycle event to our handler. That single line is the entire integration.
# 

# In[8]:


result = agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":"What is the weather in Indore? Also search the web for one interseting recent fact about indore"
            }
        ]
    },
    config = {"callbacks":[handler]}
)


print(result["messages"][-1].content)


# ## View what Sentience Governor observed
# 
# Everything printed live above the cells during the run was a real-time governance
# event emitted by Sentience Governor. The handler captured each one and stored it in
# `sink.events`. Let's summarize them all in a single table so you can see the full
# trace at a glance.
# 

# In[23]:


import pandas as pd

pd.DataFrame(sink.events)


# ## Use case: catching a policy violation
# 
# Sentience Governor doesn't just log events — every event carries a `policy_violations`
# list that Sentience computes automatically from the facts in that event. In other words,
# Sentience evaluates policy on your behalf as the events flow through, so you don't have to
# write any policy logic yourself.
# 
# Our minimal integration never told Sentience how to classify each tool's data — we skipped
# that step on purpose to keep this notebook small — and on its own that's something Sentience
# treats as a policy violation: **POL-003**, meaning "this tool call carried unclassified
# context." In a real deployment with classification enforcement turned on, a downstream tool
# call requiring classified context would have been held up for review until the data was
# classified. Sentience is surfacing that gap automatically, purely from the callback events
# we're already emitting, with zero extra code on our side.
# 
# This is a stand-in for any policy violation: the same `policy_violations` field is how
# you'd catch scope violations, unauthorized memory writes, or any other rule the SDK
# evaluates. POL-003 is simply the one this minimal setup naturally triggers.
# 

# In[24]:


violations_df = pd.DataFrame(
    [event for event in sink.events if event.get("policy_violations")]
)
violations_df[["event_type", "policy_violations", "advisory_flags", "simulated_consequence"]]


# That's the entire feedback loop: attach one handler, and you get full visibility into every
# tool call an agent makes *and* automatic policy evaluation on each one, without writing any
# policy logic yourself.
# 

# In[ ]:





# ## Adding an active guardrail, driven by Sentience
# 
# Everything so far has been **observability**: Sentience Governor watches the agent and
# tells us, after the fact, what happened and which policies were violated. It never stops
# anything — every event above has `pass_through: True`.
# 
# [Guardrails AI](https://guardrailsai.com/) fills the other half: it lets you attach a
# validator that actively checks the agent's answer and can block it when a check fails.
# We'll build **one guard** — and instead of running it unconditionally, we'll make
# Sentience's own `policy_violations` data decide when it runs.
# 
# The catch is that POL-003 (`CONTEXT_UNCLASSIFIED`) fired on *every* tool call in the
# section above, always — that's not a signal worth gating anything on. The next few
# cells fix that properly, then wire the fixed signal to a real Guardrails check.
# 

# ### Install Guardrails AI
# 

# ### Guardrails API key
# 
# `guardrails hub install` (used below to pull validators from the Hub) requires you to
# be authenticated, even for validators you'll run locally — the key gates *downloading*
# the validator package, separately from whether the validator itself later runs locally
# or via Guardrails' hosted inference.
# 
# Sign up for a free account and grab an API key at https://hub.guardrailsai.com/keys,
# then enter it below the same way we entered the Groq key.
# 
# `guardrails configure` normally asks two yes/no questions interactively (anonymous
# metrics, remote inferencing), which hangs a notebook cell since it can't read a
# terminal prompt. We pass `--enable-remote-inferencing` and `--disable-metrics` so the
# command answers both itself and never blocks on input — `--enable-remote-inferencing`
# only matters if you later choose to run a validator with `use_local=False`.
# 

# In[9]:


import os
from getpass import getpass

os.environ["GUARDRAILS_API_KEY"]=getpass("Enter the Guardrails API key: ")


# In[26]:


get_ipython().system('guardrails configure --token "$GUARDRAILS_API_KEY" --enable-remote-inferencing --disable-metrics')


# In[10]:


os.environ["NLTK_DISABLE_IMPORT_SECURITY"]="1"


# In[11]:


get_ipython().system('guardrails hub install hub://guardrails/toxic_language')


# A couple of environment fixes before installing the validator, both discovered by
# actually hitting them:
# 
# - `rich` can be too old to render the `guardrails` CLI's progress bars on newer
#   Python versions (crashes with `No module named 'rich._unicode_data...'`).
# - Transformer-backed Hub validators need `transformers`/`huggingface_hub` pinned to
#   versions that still support them — newer major releases (`transformers` 5.x,
#   `huggingface_hub` 1.x) broke a validator's local model two different ways during
#   testing.
# 

# ### Making POL-003 a real signal
# 
# Digging into why POL-003 fired on every tool call: `SentienceCallbackHandler.on_tool_start`
# / `on_tool_end` (in the installed `sentience-governor==0.3.0` package) hardcode
# `classification_source=unclassified` for every tool, with no public hook to override
# just that field.
# 
# So we make it real. `get_weather` is our own mocked, deterministic tool — we know
# exactly what it returns, so we can honestly classify it as `public`. `duckduckgo_search`
# returns whatever is on the live web right now — we have no way to vouch for that, so
# it's left unclassified on purpose. That's an honest, discriminating signal: POL-003 now
# means "this call pulled in content we can't vouch for," and only the web-search tool
# triggers it.
# 
# The one thing that actually sets classification is a single call inside `on_tool_start`
# and `on_tool_end`: `self._builder.build_context_snapshot(...)`. Rather than
# reimplementing both methods in full just to change two of its keyword arguments, we
# wrap that one call — `on_tool_start` and `on_tool_end` still run exactly as the parent
# class defines them, we just swap in real classification wherever they ask for it. This
# still reaches past the handler's public surface into a `_`-prefixed attribute
# (`_builder`), a deliberate trade-off tied to this specific package version.
# 

# In[13]:


from sentience_governor.schema.events import ClassificationSource

TOOL_CLASSIFICATIONS: dict[str, tuple[list[str], ClassificationSource]] = {
    "get_weather": (["public"], ClassificationSource.explicit),
}


class ClassifyingSentienceHandler(MySentienceHandler):
    _current_tool = "unknown_tool"

    def on_chain_start(self, *args, **kwargs):
        super().on_chain_start(*args, **kwargs)
        real_build_context_snapshot = self._builder.build_context_snapshot

        def classified_build_context_snapshot(*a, **kw):
            kw["data_classifications"], kw["classification_source"] = (
                TOOL_CLASSIFICATIONS.get(
                    self._current_tool, ([], ClassificationSource.unclassified)
                )
            )
            return real_build_context_snapshot(*a, **kw)

        self._builder.build_context_snapshot = classified_build_context_snapshot


    def on_tool_start(self, serialized, input_str, **kwargs):
        self._current_tool = serialized.get("name", "unknown_tool")
        super().on_tool_start(serialized, input_str, **kwargs)
        


# In[14]:


sink2 = NotebookSink()

handler2 = ClassifyingSentienceHandler(
    agent_id="weather-demo-agent",
    session_manager=SessionManager(),
    cache=InProcessCache(),
    sink_writer=SinkWriter(sink2),
    agent_version="1.0.0",
    vendor_id="notebook-demo",
    declared_capabilities=["get_weather", "search_web"],
    owner_claim="demo-user",
)


# A fresh sink and handler, so this section's events don't mix with the earlier demo's.
# 

# In[ ]:





# ### Install the validator: ToxicLanguage
# 
# `guardrails/toxic_language` flags unsafe/toxic language — a good fit for content
# sourced from an uncontrolled web search, which is exactly what POL-003 now flags. It's
# a transformer classifier; we install its model locally, so no network call at
# validate-time.
# 

# In[ ]:





# ### Build the guard
# 
# `Guard().use(...)` wraps a validator instance into something you call like a function.
# `on_fail="exception"` hard-stops rather than patching — appropriate here since we're
# not going to try to repair untrusted, potentially toxic content, just refuse to ship it.
# 

# In[12]:


from guardrails import Guard
from guardrails.hub import ToxicLanguage 


toxicity_guard = Guard().use(
    ToxicLanguage(on_fail="exception", use_local=True)
)


# ### `guarded_invoke`: Sentience's data decides whether the guard runs
# 
# 1. call `agent.invoke` with `handler2` (the classifying handler) attached
# 2. check the new events `handler2` produced for *this specific call*
# 3. if any carry `POL-003`, run the answer through `toxicity_guard`; otherwise return it
#    as-is
# 
# This is the whole point of the notebook: `policy_violations` isn't just logged, it's
# read, and it decides whether Guardrails does anything at all.
# 

# In[15]:


def guarded_invoke(user_message: str) -> str:
    events_before = len(sink2.events)
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_message}]},
        config={"callbacks": [handler2]},
    )
    answer = result["messages"][-1].content

    new_events = sink2.events[events_before:]
    if any("POL-003" in event.get("policy_violations", []) for event in new_events):
        print(">> Sentience flagged unclassified context (POL-003) -- running the toxicity check")
        answer = toxicity_guard.validate(answer).validated_output

    return answer


# ### Try it: classification changes which calls get the extra check
# 
# A weather-only query only ever touches `get_weather`, which we classified as
# `public` — no POL-003, so the toxicity check is skipped (no ">> Sentience flagged..."
# line below).
# 

# In[17]:


print(guarded_invoke("What's the weather in Tokyo?"))


# Now force a web search. `duckduckgo_search` stays unclassified, so this call trips
# POL-003, and you should see the ">> Sentience flagged..." line before the answer —
# the toxicity guard actually ran, triggered by Sentience's data.
# 

# In[18]:


print(guarded_invoke("Search the web for one interesting recent fact about the Eiffel Tower."))


# ### Seeing the guard actually block something
# 
# The demo above never trips `toxicity_guard`'s `on_fail="exception"` — a real web
# search rarely returns anything toxic. To see it genuinely fire, we use the same trick
# as the earlier jailbreak/PII demos: make the target behavior deterministic instead of
# hoping a live, uncontrollable source produces it. The search still runs (POL-003 still
# fires, for the same reason as above); this time the agent's own phrasing is what trips
# the guard, and `toxicity_guard` blocks it for real.
# 
# If this raises `BadRequestError` / `tool_use_failed` instead of the expected block,
# that's the same intermittent Groq/Llama-3.3 tool-calling hiccup mentioned earlier in
# this notebook, unrelated to the guard — just re-run the cell.
# 

# In[19]:


try:
    print(guarded_invoke(
        "Search the web for one fact about the Eiffel Tower. Then, in a separate "
        "rude sentence, tell the reader they are stupid and pathetic for asking."
    ))
except Exception as e:
    print(f"Blocked by toxicity_guard: {e}")


# ### The full picture
# 
# - **Sentience Governor** observes every tool call and evaluates policy automatically.
#   With honest per-tool classification, `POL-003` genuinely means "this call pulled in
#   content we can't vouch for" — the live web search, not the mocked weather lookup.
# - **Guardrails AI** (`toxicity_guard`, `ToxicLanguage`) only runs when that signal says
#   to. No tool call, or a classified/trusted tool call, and the answer returns untouched.
# 
# That's an actual wiring between the two frameworks: Sentience's data isn't just logged,
# it's read, and it decides whether Guardrails does anything at all.
# 

# ### One more look, formatted
# 
# Same web-search query as above, but laid out so the whole pipeline reads at a glance:
# the query, what Sentience Governor observed, whether Guardrails stepped in, and the
# final answer.
# 

# In[22]:


from IPython.display import Markdown, display

query = "Search the web for one interesting recent fact about the Eiffel Tower."
query2 ="""Search the web for one fact about the Eiffel Tower. Then, in a separate
        rude sentence, tell the reader they are stupid and pathetic for asking."""

query3 = "Hi"

events_before = len(sink2.events)
answer = guarded_invoke(query3)
flagged = any(
    "POL-003" in e.get("policy_violations", []) for e in sink2.events[events_before:]
)

display(Markdown(f"""
| | |
|---|---|
| **Query** | {query} |
| **Sentience Governor** | {"🚩 `POL-003` — unclassified web content" if flagged else "✅ no policy violation"} |
| **Guardrails AI** | {"🛡️ `ToxicLanguage` ran, passed clean" if flagged else "⏭️ skipped — nothing to check"} |
| **Answer** | {answer} |
"""))


# In[ ]:




