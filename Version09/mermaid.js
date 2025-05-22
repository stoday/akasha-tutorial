flowchart TD
    subgraph "Frontend Layer"
        CLI["CLI"]:::frontend
        UI["Streamlit UI"]:::frontend
        API["HTTP API"]:::frontend
    end

    subgraph "Core Orchestrator"
        DocQA["Document QA"]:::core
        Agent["Agent Module"]:::core
        Eval["Evaluation"]:::core
        Summary["Summarization"]:::core
        Helper["Helper"]:::core
        Format["Format"]:::core
        Prompts["Prompts"]:::core
        Search["Search"]:::core
        SelfQuery["Self-Query"]:::core
    end

    subgraph "Data Layer"
        VectorDB["ChromaDB Store"]:::data
        FileStore["File Store (docs/)"]:::data
        JSONOut["JSON Outputs"]:::data
    end

    subgraph "Model & Embeddings"
        OpenAI["OpenAI/Azure Adapter"]:::adapter
        HF["HuggingFace Adapter"]:::adapter
        LLAMA["llama-cpp Adapter"]:::adapter
        Anthropic["Anthropic Adapter"]:::adapter
        Gemini["Gemini Adapter"]:::adapter
        ChatGLM["ChatGLM Adapter"]:::adapter
        Custom["Other Adapters"]:::adapter
    end

    subgraph "External Services"
        ExtOpenAI["OpenAI API"]:::external
        ExtAzure["Azure OpenAI API"]:::external
        ExtHFHub["HuggingFace Hub"]:::external
        Wiki["Wikipedia API"]:::external
    end

    subgraph "DevOps & Deployment"
        Docker["Dockerfiles & Containers"]:::devops
        CI["CI Pipeline"]:::devops
        Packaging["Setup & Requirements"]:::devops
    end

    CLI -->|Query| DocQA
    UI -->|Query| DocQA
    API -->|Request| DocQA

    DocQA -->|uses| Helper
    DocQA -->|formats| Format
    DocQA -->|constructs| Prompts
    DocQA -->|calls| Search
    DocQA -->|self-query| SelfQuery
    Search -->|Query→Retrieve| VectorDB
    SelfQuery -->|Self-Query→Retrieve| VectorDB
    DocQA -->|read/write| FileStore
    DocQA -->|outputs| JSONOut
    DocQA -->|evaluate| Eval
    DocQA -->|summarize| Summary

    DocQA -->|prompt| OpenAI
    DocQA -->|prompt| HF
    DocQA -->|prompt| LLAMA
    DocQA -->|prompt| Anthropic
    DocQA -->|prompt| Gemini
    DocQA -->|prompt| ChatGLM
    DocQA -->|prompt| Custom

    OpenAI -->|API call| ExtOpenAI
    Anthropic -->|API call| ExtAzure
    HF -->|API call| ExtHFHub
    LLAMA -->|Local Engine| 
    Agent -->|tool calls| JSONOut
    Agent -->|wiki lookup| Wiki

    click CLI "https://github.com/iii-org/akasha/blob/master/cli/glue.py"
    click UI "https://github.com/iii-org/akasha/blob/master/akasha/ui.py"
    click API "https://github.com/iii-org/akasha/blob/master/akasha/api.py"
    click DocQA "https://github.com/iii-org/akasha/blob/master/akasha/akashas.py"
    click Agent "https://github.com/iii-org/akasha/blob/master/akasha/agents.py"
    click Eval "https://github.com/iii-org/akasha/blob/master/akasha/eval/eval.py"
    click Summary "https://github.com/iii-org/akasha/blob/master/akasha/summary.py"
    click Helper "https://github.com/iii-org/akasha/blob/master/akasha/helper.py"
    click Format "https://github.com/iii-org/akasha/blob/master/akasha/format.py"
    click Prompts "https://github.com/iii-org/akasha/blob/master/akasha/prompts.py"
    click Search "https://github.com/iii-org/akasha/blob/master/akasha/search.py"
    click SelfQuery "https://github.com/iii-org/akasha/blob/master/akasha/self_query.py"
    click VectorDB "https://github.com/iii-org/akasha/blob/master/akasha/db.py"
    click OpenAI "https://github.com/iii-org/akasha/blob/master/akasha/models/anthro.py"
    click HF "https://github.com/iii-org/akasha/blob/master/akasha/models/hf.py"
    click LLAMA "https://github.com/iii-org/akasha/blob/master/akasha/models/llamacpp2.py"
    click Anthropic "https://github.com/iii-org/akasha/blob/master/akasha/models/anthro.py"
    click Gemini "https://github.com/iii-org/akasha/blob/master/akasha/models/gemi.py"
    click ChatGLM "https://github.com/iii-org/akasha/blob/master/akasha/models/chglm.py"
    click Custom "https://github.com/iii-org/akasha/blob/master/akasha/models/custom.py"
    click Docker "https://github.com/iii-org/akasha/tree/master/Dockerfile"
    click CI "https://github.com/iii-org/akasha/blob/master/.gitlab-ci.yml"
    click Packaging "https://github.com/iii-org/akasha/blob/master/setup.py"

    classDef frontend fill:#9fc5e8,stroke:#5b9bd5
    classDef core fill:#ffe599,stroke:#d79d00
    classDef data fill:#b6d7a8,stroke:#38761d
    classDef adapter fill:#f9cb9c,stroke:#e69138
    classDef external fill:#d9d9d9,stroke:#7f7f7f
    classDef devops fill:#c9c9ff,stroke:#5555aa