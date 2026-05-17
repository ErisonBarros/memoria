---
sourceFile: "Agent Skills - Claude API Docs"
exportedBy: "Kortex"
exportDate: "2026-05-17T23:05:02.666Z"
---

# Agent Skills - Claude API Docs

9fd4cacc-c6dd-46c0-b5b4-0fafb35ffab0

Agent Skills - Claude API Docs

d727c71c-5562-419f-8982-5e37cae889b5

https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview

Agent Skills - Claude API Docs

https://platform.claude.com/docs/pt-BR/home

https://platform.claude.com/docs/pt-BR/intro

https://platform.claude.com/docs/pt-BR/build-with-claude/administration-api

Modelos e preços

https://platform.claude.com/docs/pt-BR/about-claude/models/overview

SDKs do cliente

https://platform.claude.com/docs/pt-BR/api/client-sdks

Referência da API

https://platform.claude.com/docs/pt-BR/api/overview

API reference

https://platform.claude.com/docs/pt-BR/api/overview

Português (BR)

https://platform.claude.com/

https://platform.claude.com/login?returnTo=%2Fdocs%2Fpt-BR%2Fagents-and-tools%2Fagent-skills%2Foverview

https://platform.claude.com/login

Visão geral

Construir/ Skills

Agent Skills

Agent Skills são capacidades modulares que estendem a funcionalidade do Claude. Cada Skill empacota instruções, metadados e recursos opcionais (scripts, templates) que o Claude usa automaticamente quando relevante.

This feature is

eligible for

Zero Data Retention (ZDR)

https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention

. Data is retained according to the feature's standard retention policy.

Por que usar Skills

Skills são recursos reutilizáveis baseados em sistema de arquivos que fornecem ao Claude expertise específica de domínio: fluxos de trabalho, contexto e melhores práticas que transformam agentes de uso geral em especialistas. Ao contrário de prompts (instruções no nível de conversa para tarefas pontuais), Skills carregam sob demanda e eliminam a necessidade de fornecer repetidamente as mesmas orientações em múltiplas conversas.

Principais benefícios

Especializar o Claude

: Adaptar capacidades para tarefas específicas de domínio

Reduzir repetição

: Criar uma vez, usar automaticamente

Compor capacidades

: Combinar Skills para construir fluxos de trabalho complexos

Para uma análise aprofundada da arquitetura e aplicações reais de Agent Skills, leia nosso blog de engenharia:

Equipping agents for the real world with Agent Skills

https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

Usando Skills

A Anthropic fornece Agent Skills pré-construídas para tarefas comuns de documentos (PowerPoint, Excel, Word, PDF), e você pode criar suas próprias Skills personalizadas. Ambas funcionam da mesma forma. O Claude as usa automaticamente quando relevante para sua solicitação.

Agent Skills pré-construídas

estão disponíveis para todos os usuários no claude.ai e via Claude API. Veja a seção

Skills Disponíveis

https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#available-skills

abaixo para a lista completa.

Skills personalizadas

permitem que você empacote expertise de domínio e conhecimento organizacional. Elas estão disponíveis nos produtos do Claude: crie-as no Claude Code, faça upload via API ou adicione-as nas configurações do claude.ai.

#### Comece agora:

Para Agent Skills pré-construídas: Veja o

tutorial de início rápido

https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/quickstart

para começar a usar as skills de PowerPoint, Excel, Word e PDF na API

Para Skills personalizadas: Veja o

Agent Skills Cookbook

https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction

para aprender como criar suas próprias Skills

Como as Skills funcionam

As Skills aproveitam o ambiente de VM do Claude para fornecer capacidades além do que é possível apenas com prompts. O Claude opera em uma máquina virtual com acesso ao sistema de arquivos, permitindo que as Skills existam como diretórios contendo instruções, código executável e materiais de referência, organizados como um guia de integração que você criaria para um novo membro da equipe.

Essa arquitetura baseada em sistema de arquivos permite a

divulgação progressiva

: o Claude carrega informações em etapas conforme necessário, em vez de consumir contexto antecipadamente.

Três tipos de conteúdo de Skill, três níveis de carregamento

As Skills podem conter três tipos de conteúdo, cada um carregado em momentos diferentes:

Nível 1: Metadados (sempre carregados)

Tipo de conteúdo: Instruções

. O frontmatter YAML da Skill fornece informações de descoberta:

---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---

O Claude carrega esses metadados na inicialização e os inclui no prompt do sistema. Essa abordagem leve significa que você pode instalar muitas Skills sem penalidade de contexto; o Claude apenas sabe que cada Skill existe e quando usá-la.

Nível 2: Instruções (carregadas quando acionadas)

Tipo de conteúdo: Instruções

. O corpo principal do SKILL.md contém conhecimento procedural: fluxos de trabalho, melhores práticas e orientações:

# PDF Processing

## Quick start

Use pdfplumber to extract text from PDFs:

\`\`\`python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages\[0\].extract\_text()

For advanced form filling, see

Quando você solicita algo que corresponde à descrição de uma Skill, o Claude lê o SKILL.md do sistema de arquivos via bash. Somente então esse conteúdo entra na janela de contexto.

### Nível 3: Recursos e código (carregados conforme necessário)

\*\*Tipos de conteúdo: Instruções, código e recursos\*\*. As Skills podem incluir materiais adicionais:

├── SKILL.md (main instructions)

├── FORMS.md (form-filling guide)

├── REFERENCE.md (detailed API reference)

└── scripts/

└── fill\_form.py (utility script)

\*\*Instruções\*\*: Arquivos markdown adicionais (FORMS.md, REFERENCE.md) contendo orientações especializadas e fluxos de trabalho

\*\*Código\*\*: Scripts executáveis (fill\_form.py, validate.py) que o Claude executa via bash; scripts fornecem operações determinísticas sem consumir contexto

\*\*Recursos\*\*: Materiais de referência como esquemas de banco de dados, documentação de API, templates ou exemplos

O Claude acessa esses arquivos apenas quando referenciados. O modelo de sistema de arquivos significa que cada tipo de conteúdo tem diferentes pontos fortes: instruções para orientação flexível, código para confiabilidade, recursos para consulta factual.

| Nível | Quando Carregado | Custo em Tokens | Conteúdo |
| --- | --- | --- | --- |
| \*\*Nível 1: Metadados\*\* | Sempre (na inicialização) | ~100 tokens por Skill | \`name\` e \`description\` do frontmatter YAML |
| \*\*Nível 2: Instruções\*\* | Quando a Skill é acionada | Menos de 5k tokens | Corpo do SKILL.md com instruções e orientações |
| \*\*Nível 3+: Recursos\*\* | Conforme necessário | Efetivamente ilimitado | Arquivos incluídos executados via bash sem carregar conteúdo no contexto |

A divulgação progressiva garante que apenas o conteúdo relevante ocupe a janela de contexto em qualquer momento.

### A arquitetura de Skills

As Skills são executadas em um ambiente de execução de código onde o Claude tem acesso ao sistema de arquivos, comandos bash e capacidades de execução de código. Pense assim: as Skills existem como diretórios em uma máquina virtual, e o Claude interage com elas usando os mesmos comandos bash que você usaria para navegar em arquivos no seu computador.
!\[Arquitetura de Agent Skills - mostrando como as Skills se integram com a configuração do agente e a máquina virtual\](https://platform.claude.com/docs/images/agent-skills-architecture.png)

\*\*Como o Claude acessa o conteúdo da Skill:\*\*

Quando uma Skill é acionada, o Claude usa bash para ler o SKILL.md do sistema de arquivos, trazendo suas instruções para a janela de contexto. Se essas instruções referenciam outros arquivos (como FORMS.md ou um esquema de banco de dados), o Claude lê esses arquivos também usando comandos bash adicionais. Quando as instruções mencionam scripts executáveis, o Claude os executa via bash e recebe apenas a saída (o código do script em si nunca entra no contexto).

\*\*O que essa arquitetura permite:\*\*

\*\*Acesso a arquivos sob demanda\*\*: O Claude lê apenas os arquivos necessários para cada tarefa específica. Uma Skill pode incluir dezenas de arquivos de referência, mas se sua tarefa precisar apenas do esquema de vendas, o Claude carrega apenas esse arquivo. O restante permanece no sistema de arquivos consumindo zero tokens.

\*\*Execução eficiente de scripts\*\*: Quando o Claude executa \`validate\_form.py\` , o código do script nunca é carregado na janela de contexto. Apenas a saída do script (como "Validação aprovada" ou mensagens de erro específicas) consome tokens. Isso torna os scripts muito mais eficientes do que fazer o Claude gerar código equivalente dinamicamente.

\*\*Sem limite prático para conteúdo incluído\*\*: Como os arquivos não consomem contexto até serem acessados, as Skills podem incluir documentação abrangente de API, grandes conjuntos de dados, exemplos extensos ou quaisquer materiais de referência necessários. Não há penalidade de contexto para conteúdo incluído que não é usado.

Esse modelo baseado em sistema de arquivos é o que faz a divulgação progressiva funcionar. O Claude navega pela sua Skill como você referenciaria seções específicas de um guia de integração, acessando exatamente o que cada tarefa requer.

### Exemplo: Carregando uma skill de processamento de PDF

Veja como o Claude carrega e usa uma skill de processamento de PDF:

1. \*\*Inicialização\*\*: O prompt do sistema inclui: \`PDF Processing - Extract text and tables from PDF files, fill forms, merge documents\`
2. \*\*Solicitação do usuário\*\*: "Extraia o texto deste PDF e resuma-o"
3. \*\*Claude invoca\*\*: \`bash: read pdf-skill/SKILL.md\` → Instruções carregadas no contexto
4. \*\*Claude determina\*\*: O preenchimento de formulários não é necessário, portanto FORMS.md não é lido
5. \*\*Claude executa\*\*: Usa instruções do SKILL.md para concluir a tarefa
!\[Skills carregando na janela de contexto - mostrando o carregamento progressivo de metadados e conteúdo de skill\](https://platform.claude.com/docs/images/agent-skills-context-window.png)

O diagrama mostra:

1. Estado padrão com prompt do sistema e metadados de skill pré-carregados
2. Claude aciona a skill lendo SKILL.md via bash
3. Claude opcionalmente lê arquivos adicionais incluídos como FORMS.md conforme necessário
4. Claude prossegue com a tarefa

Esse carregamento dinâmico garante que apenas o conteúdo relevante da skill ocupe a janela de contexto.

## Onde as Skills funcionam

As Skills estão disponíveis nos produtos de agente do Claude:

### Claude API

A Claude API suporta tanto Agent Skills pré-construídas quanto Skills personalizadas. Ambas funcionam de forma idêntica: especifique o \`skill\_id\` relevante no parâmetro \`container\` junto com a ferramenta de execução de código.

\*\*Pré-requisitos\*\*: Usar Skills via API requer três cabeçalhos beta:

- \`code-execution-2025-08-25\` - Skills são executadas no contêiner de execução de código
- \`skills-2025-10-02\` - Habilita a funcionalidade de Skills
- \`files-api-2025-04-14\` - Necessário para fazer upload/download de arquivos para/do contêiner

Use Agent Skills pré-construídas referenciando seu \`skill\_id\` (por exemplo, \`pptx\` , \`xlsx\` ), ou crie e faça upload das suas próprias via Skills API (endpoints \`/v1/skills\` ). Skills personalizadas são compartilhadas em toda a organização.

Para saber mais, veja \[Usar Skills com a Claude API\](https://platform.claude.com/docs/pt-BR/build-with-claude/skills-guide).

### Claude Code

\[Claude Code\](https://code.claude.com/docs/en/overview) suporta apenas Skills Personalizadas.

\*\*Skills Personalizadas\*\*: Crie Skills como diretórios com arquivos SKILL.md. O Claude as descobre e usa automaticamente.

Skills personalizadas no Claude Code são baseadas em sistema de arquivos e não requerem uploads via API.

Para saber mais, veja \[Usar Skills no Claude Code\](https://code.claude.com/docs/en/skills).

### Claude.ai

\[Claude.ai\](https://claude.ai/) suporta tanto Agent Skills pré-construídas quanto Skills personalizadas.

\*\*Agent Skills pré-construídas\*\*: Essas Skills já funcionam nos bastidores quando você cria documentos. O Claude as usa sem exigir nenhuma configuração.

\*\*Skills personalizadas\*\*: Faça upload das suas próprias Skills como arquivos zip através de Configurações > Recursos. Disponível nos planos Pro, Max, Team e Enterprise com execução de código habilitada. Skills personalizadas são individuais para cada usuário; elas não são compartilhadas em toda a organização e não podem ser gerenciadas centralmente por administradores.

Para saber mais sobre como usar Skills no Claude.ai, veja os seguintes recursos no Centro de Ajuda do Claude:

- \[O que são Skills?\](https://support.claude.com/en/articles/12512176-what-are-skills)
- \[Usando Skills no Claude\](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- \[Como criar Skills personalizadas\](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- \[Ensine ao Claude sua forma de trabalhar usando Skills\](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)

## Estrutura de Skill

Toda Skill requer um arquivo \`SKILL.md\` com frontmatter YAML:

name: your-skill-name

description: Brief description of what this Skill does and when to use it

Your Skill Name

Instructions

\[Clear, step-by-step guidance for Claude to follow\]

\[Concrete examples of using this Skill\]

\*\*Campos obrigatórios\*\*: \`name\` e \`description\`

\*\*Requisitos dos campos\*\*: \`name\` :

- Máximo de 64 caracteres
- Deve conter apenas letras minúsculas, números e hífens
- Não pode conter tags XML
- Não pode conter palavras reservadas: "anthropic", "claude" \`description\` :

- Deve ser não vazio
- Máximo de 1024 caracteres
- Não pode conter tags XML

A \`description\` deve incluir tanto o que a Skill faz quanto quando o Claude deve usá-la. Para orientações completas de criação, veja o \[guia de melhores práticas\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/best-practices).

## Considerações de segurança

Recomendamos fortemente usar Skills apenas de fontes confiáveis: aquelas que você mesmo criou ou obteve da Anthropic. As Skills fornecem ao Claude novas capacidades por meio de instruções e código, e embora isso as torne poderosas, também significa que uma Skill maliciosa pode direcionar o Claude a invocar ferramentas ou executar código de maneiras que não correspondem ao propósito declarado da Skill.

Se você precisar usar uma Skill de uma fonte não confiável ou desconhecida, tome extrema cautela e audite-a completamente antes do uso. Dependendo do acesso que o Claude tem ao executar a Skill, Skills maliciosas podem levar à exfiltração de dados, acesso não autorizado ao sistema ou outros riscos de segurança.

\*\*Principais considerações de segurança\*\*:

- \*\*Audite completamente\*\*: Revise todos os arquivos incluídos na Skill: SKILL.md, scripts, imagens e outros recursos. Procure padrões incomuns como chamadas de rede inesperadas, padrões de acesso a arquivos ou operações que não correspondem ao propósito declarado da Skill
- \*\*Fontes externas são arriscadas\*\*: Skills que buscam dados de URLs externas representam risco particular, pois o conteúdo buscado pode conter instruções maliciosas. Mesmo Skills confiáveis podem ser comprometidas se suas dependências externas mudarem ao longo do tempo
- \*\*Uso indevido de ferramentas\*\*: Skills maliciosas podem invocar ferramentas (operações de arquivo, comandos bash, execução de código) de maneiras prejudiciais
- \*\*Exposição de dados\*\*: Skills com acesso a dados sensíveis podem ser projetadas para vazar informações para sistemas externos
- \*\*Trate como instalar software\*\*: Use apenas Skills de fontes confiáveis. Seja especialmente cuidadoso ao integrar Skills em sistemas de produção com acesso a dados sensíveis ou operações críticas

## Skills Disponíveis

### Agent Skills pré-construídas

As seguintes Agent Skills pré-construídas estão disponíveis para uso imediato:

- \*\*PowerPoint (pptx)\*\*: Criar apresentações, editar slides, analisar conteúdo de apresentações
- \*\*Excel (xlsx)\*\*: Criar planilhas, analisar dados, gerar relatórios com gráficos
- \*\*Word (docx)\*\*: Criar documentos, editar conteúdo, formatar texto
- \*\*PDF (pdf)\*\*: Gerar documentos PDF formatados e relatórios

Essas Skills estão disponíveis na Claude API e no claude.ai. Veja o \[tutorial de início rápido\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/quickstart) para começar a usá-las na API.

### Skills de código aberto

A Anthropic também publica Skills de código aberto no \[repositório de skills\](https://github.com/anthropics/skills):

- \*\*\[Claude API\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/claude-api-skill)\*\*: Fornece ao Claude material de referência de API atualizado, documentação de SDK e melhores práticas para 8 linguagens de programação. Incluído com o Claude Code e também disponível para instalação a partir do repositório de skills.

### Exemplos de Skills personalizadas

Para exemplos completos de Skills personalizadas, veja o \[cookbook de Skills\](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction).

## Retenção de dados

Agent Skills não é coberto por acordos ZDR. Definições de Skills e dados de execução são retidos de acordo com a política padrão de retenção de dados da Anthropic.

Para elegibilidade ZDR em todos os recursos, veja \[API e retenção de dados\](https://platform.claude.com/docs/pt-BR/build-with-claude/api-and-data-retention).

## Limitações e restrições

Entender essas limitações ajuda você a planejar sua implantação de Skills de forma eficaz.

### Disponibilidade entre superfícies

\*\*Skills personalizadas não sincronizam entre superfícies\*\*. Skills carregadas em uma superfície não estão automaticamente disponíveis em outras:

- Skills carregadas no Claude.ai devem ser carregadas separadamente na API
- Skills carregadas via API não estão disponíveis no Claude.ai
- Skills do Claude Code são baseadas em sistema de arquivos e separadas tanto do Claude.ai quanto da API

Você precisará gerenciar e fazer upload de Skills separadamente para cada superfície onde deseja usá-las.

### Escopo de compartilhamento

As Skills têm diferentes modelos de compartilhamento dependendo de onde você as usa:

- \*\*Claude.ai\*\*: Apenas usuário individual; cada membro da equipe deve fazer upload separadamente
- \*\*Claude API\*\*: Em todo o workspace; todos os membros do workspace podem acessar as Skills carregadas
- \*\*Claude Code\*\*: Pessoal ( \`~/.claude/skills/\` ) ou baseado em projeto ( \`.claude/skills/\` ); também pode ser compartilhado via Claude Code Plugins

O Claude.ai atualmente não suporta gerenciamento centralizado de administrador ou distribuição de Skills personalizadas em toda a organização.

### Restrições do ambiente de execução

O ambiente de execução exato disponível para sua skill depende da superfície do produto onde você a usa.

- \*\*Claude.ai\*\*:

    - \*\*Acesso à rede variável\*\*: Dependendo das configurações do usuário/administrador, as Skills podem ter acesso total, parcial ou nenhum acesso à rede. Para mais detalhes, veja o artigo de suporte \[Criar e Editar Arquivos\](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h\_6b7e833898).
- \*\*Claude API\*\*:

    - \*\*Sem acesso à rede\*\*: Skills não podem fazer chamadas de API externas ou acessar a internet
    - \*\*Sem instalação de pacotes em tempo de execução\*\*: Apenas pacotes pré-instalados estão disponíveis. Você não pode instalar novos pacotes durante a execução.
    - \*\*Apenas dependências pré-configuradas\*\*: Verifique a \[documentação da ferramenta de execução de código\](https://platform.claude.com/docs/pt-BR/agents-and-tools/tool-use/code-execution-tool) para a lista de pacotes disponíveis
- \*\*Claude Code\*\*:

    - \*\*Acesso total à rede\*\*: Skills têm o mesmo acesso à rede que qualquer outro programa no computador do usuário
    - \*\*Instalação global de pacotes desencorajada\*\*: Skills devem instalar pacotes apenas localmente para evitar interferir no computador do usuário

Planeje suas Skills para funcionar dentro dessas restrições.

## Próximos passos

\[Começar com Agent Skills Crie sua primeira Skill\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/quickstart)

\[Guia de API Usar Skills com a Claude API\](https://platform.claude.com/docs/pt-BR/build-with-claude/skills-guide)

\[Usar Skills no Claude Code Criar e gerenciar Skills personalizadas no Claude Code\](https://code.claude.com/docs/en/skills)

\[Melhores práticas de criação Escrever Skills que o Claude pode usar efetivamente\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/best-practices)

Was this page helpful?

- \[Por que usar Skills\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#por-que-usar-skills)
- \[Usando Skills\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#usando-skills)
- \[Como as Skills funcionam\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#como-as-skills-funcionam)
- \[Três tipos de conteúdo de Skill, três níveis de carregamento\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#tres-tipos-de-conteudo-de-skill-tres-niveis-de-carregamento)
- \[Nível 1: Metadados (sempre carregados)\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#nivel-1-metadados-sempre-carregados)
- \[Nível 2: Instruções (carregadas quando acionadas)\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#nivel-2-instrucoes-carregadas-quando-acionadas)
- \[Nível 3: Recursos e código (carregados conforme necessário)\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#nivel-3-recursos-e-codigo-carregados-conforme-necessario)
- \[A arquitetura de Skills\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#a-arquitetura-de-skills)
- \[Exemplo: Carregando uma skill de processamento de PDF\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#exemplo-carregando-uma-skill-de-processamento-de-pdf)
- \[Onde as Skills funcionam\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#onde-as-skills-funcionam)
- \[Claude API\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#claude-api)
- \[Claude Code\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#claude-code)
- \[Claude.ai\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#claude-ai)
- \[Estrutura de Skill\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#estrutura-de-skill)
- \[Considerações de segurança\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#consideracoes-de-seguranca)
- \[Skills Disponíveis\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#skills-disponiveis)
- \[Agent Skills pré-construídas\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#agent-skills-pre-construidas)
- \[Skills de código aberto\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#skills-de-codigo-aberto)
- \[Exemplos de Skills personalizadas\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#exemplos-de-skills-personalizadas)
- \[Retenção de dados\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#retencao-de-dados)
- \[Limitações e restrições\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#limitacoes-e-restricoes)
- \[Disponibilidade entre superfícies\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#disponibilidade-entre-superficies)
- \[Escopo de compartilhamento\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#escopo-de-compartilhamento)
- \[Restrições do ambiente de execução\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#restricoes-do-ambiente-de-execucao)
- \[Próximos passos\](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview#proximos-passos) \[\](https://platform.claude.com/docs) \[\](https://x.com/claudeai) \[\](https://www.linkedin.com/showcase/claude) \[\](https://instagram.com/claudeai)

### Solutions

- \[AI agents\](https://claude.com/solutions/agents)
- \[Code modernization\](https://claude.com/solutions/code-modernization)
- \[Coding\](https://claude.com/solutions/coding)
- \[Customer support\](https://claude.com/solutions/customer-support)
- \[Education\](https://claude.com/solutions/education)
- \[Financial services\](https://claude.com/solutions/financial-services)
- \[Government\](https://claude.com/solutions/government)
- \[Life sciences\](https://claude.com/solutions/life-sciences)

### Partners

- \[Amazon Bedrock\](https://claude.com/partners/amazon-bedrock)
- \[Google Cloud's Vertex AI\](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- \[Blog\](https://claude.com/blog)
- \[Courses\](https://www.anthropic.com/learn)
- \[Use cases\](https://claude.com/resources/use-cases)
- \[Connectors\](https://claude.com/partners/mcp)
- \[Customer stories\](https://claude.com/customers)
- \[Engineering at Anthropic\](https://www.anthropic.com/engineering)
- \[Events\](https://www.anthropic.com/events)
- \[Powered by Claude\](https://claude.com/partners/powered-by-claude)
- \[Service partners\](https://claude.com/partners/services)
- \[Startups program\](https://claude.com/programs/startups)

### Company

- \[Anthropic\](https://www.anthropic.com/company)
- \[Careers\](https://www.anthropic.com/careers)
- \[Economic Futures\](https://www.anthropic.com/economic-futures)
- \[Research\](https://www.anthropic.com/research)
- \[News\](https://www.anthropic.com/news)
- \[Responsible Scaling Policy\](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- \[Security and compliance\](https://trust.anthropic.com/)
- \[Transparency\](https://www.anthropic.com/transparency)

### Learn

- \[Blog\](https://claude.com/blog)
- \[Courses\](https://www.anthropic.com/learn)
- \[Use cases\](https://claude.com/resources/use-cases)
- \[Connectors\](https://claude.com/partners/mcp)
- \[Customer stories\](https://claude.com/customers)
- \[Engineering at Anthropic\](https://www.anthropic.com/engineering)
- \[Events\](https://www.anthropic.com/events)
- \[Powered by Claude\](https://claude.com/partners/powered-by-claude)
- \[Service partners\](https://claude.com/partners/services)
- \[Startups program\](https://claude.com/programs/startups)

### Help and security

- \[Availability\](https://www.anthropic.com/supported-countries)
- \[Status\](https://status.claude.com/)
- \[Support\](https://support.claude.com/)
- \[Discord\](https://www.anthropic.com/discord)

### Terms and policies

- \[Privacy policy\](https://www.anthropic.com/legal/privacy)
- \[Responsible disclosure policy\](https://www.anthropic.com/responsible-disclosure-policy)
- \[Terms of service: Commercial\](https://www.anthropic.com/legal/commercial-terms)
- \[Terms of service: Consumer\](https://www.anthropic.com/legal/consumer-terms)
- \[Usage policy\](https://www.anthropic.com/legal/aup)

Ask Docs

