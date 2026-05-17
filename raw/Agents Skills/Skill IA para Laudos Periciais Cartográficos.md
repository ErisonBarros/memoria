---
sourceFile: "Skill IA para Laudos Periciais Cartográficos"
exportedBy: "Kortex"
exportDate: "2026-05-17T23:05:02.675Z"
---

# Skill IA para Laudos Periciais Cartográficos

9f6e5a2a-a817-4fe1-8b8a-58e49062d6b0

Skill IA para Laudos Periciais Cartográficos

afe425cb-d231-4779-a403-1c80dc8beefa

c\_09f3df80e3aa729a

Criar uma skill

Com base nos documentos fornecidos, a criação de uma

(habilidade) para agentes de Inteligência Artificial segue um formato padrão e estruturado, geralmente utilizando arquivos Markdown (.md).

#### Aqui estão as diretrizes principais para criar uma skill:

1. O que é uma Skill?

Uma skill é uma capacidade reutilizável que instrui agentes de IA sobre como executar tarefas específicas através de padrões, ferramentas e templates. Elas permitem que o agente atue com maior contexto, evitando erros ou alucinações.

2. Estrutura de um Arquivo

Toda skill deve começar com um arquivo chamado

, que contém metadados e instruções detalhadas. A estrutura básica inclui:

#### YAML Frontmatter (Obrigatório):

#### Localizado no topo do arquivo, deve conter:

Um identificador curto para a skill.

description:

Uma explicação de quando o agente deve usar esta skill.

#### Corpo do Markdown:

Instruções objetivas sobre como executar a tarefa. Não há restrições rígidas, mas recomenda-se clareza e objetividade.

3. Elementos Adicionais

#### Dependendo da complexidade, uma skill pode incluir:

#### Ferramentas MCP (Model Context Protocol):

Funções individuais específicas que a skill disponibiliza (ex: buscar documentação, pesquisar código).

#### Scripts de Execução:

Scripts que fornecem acesso direto às funcionalidades (como scripts Python para chamadas de API).

#### Templates e Referências:

Modelos de saída (como o template de um laudo pericial) e materiais de suporte.

4. Exemplo de Estrutura (PeritoGeo AI)

O documento "PeritoGeo AI" exemplifica uma skill completa organizada da seguinte forma:

Gerar laudos periciais automáticos.

#### Inputs (Perguntas):

Uma lista de dados que a IA deve sempre solicitar ao usuário (Número do processo, CREA, metodologia, etc.).

#### Lógica da IA:

Regras que definem o que a IA deve escrever em situações específicas (ex: se faltar documentação, deve apontar falha técnica).

#### Fundamentação Legal:

Citações obrigatórias de leis e artigos relevantes (CPC, Lei 6.015/73).

#### Template de Saída:

A estrutura exata que o documento final deve ter.

5. Como Implementar

#### As skills podem ser instaladas ou adicionadas a diferentes ecossistemas:

#### Terminal/CLI:

Usando comandos como

$ npx skills add <owner/repo>

#### Plataformas de IA:

Integração direta com ChatGPT (Custom GPTs), Claude ou via API da OpenAI.

progressive disclosure:

Os agentes carregam apenas o nome e a descrição inicialmente; a skill completa só é lida quando a tarefa corresponde à descrição, o que economiza tokens e mantém a rapidez.

