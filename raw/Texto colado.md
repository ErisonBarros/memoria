---
sourceFile: "Texto colado"
exportedBy: "Kortex"
exportDate: "2026-05-17T23:05:02.675Z"
---

# Texto colado

8ff30989-f72f-4ed3-a89f-64505c661710

Texto colado

55dd6831-6519-4355-8112-c5ed087c2296

Estrutura de uma skill

Com base nas fontes fornecidas, uma "skill" (habilidade) no contexto de agentes de Inteligência Artificial é uma capacidade reutilizável que aprimora o agente dando-lhe acesso a conhecimentos procedimentais \[Source: 1: The Agent Skills Directory\] .Analisando o exemplo específico da skill read-github (do ecossistema de skills para agentes), a estrutura de uma skill geralmente é composta pelos seguintes elementos:Instalação: As skills são instaladas através de um comando simples no terminal, seguindo o formato padrão $ npx skills add <owner/repo> \[Source: 1: The Agent Skills Directory\] .Documentação (SKILL.md): Um arquivo de documentação que descreve o que a skill faz e fornece instruções detalhadas de como o agente ou usuário deve utilizá-la \[Source: 2: read-github by am-will/codex-skills\] .Scripts de Execução (Interface de Linha de Comando - CLI): Scripts (como o scripts/gitmcp.py no exemplo do GitHub) que fornecem acesso direto às funcionalidades da skill, permitindo listar ferramentas, buscar documentações, pesquisar códigos ou fazer chamadas diretas \[Source: 2: read-github by am-will/codex-skills\] \[Source: Mostrar citações adicionais\] .Ferramentas MCP (Model Context Protocol): São as funções individuais e específicas que a skill disponibiliza. Na skill read-github, as ferramentas disponíveis são \[Source: 4: read-github by am-will/codex-skills\] :Buscar a documentação completa (fetch\_documentation).Fazer busca semântica na documentação (search\_documentation).Pesquisar código exato via API (search\_code).Buscar conteúdo de URLs genéricas mencionadas nos documentos (fetch\_generic\_url\_content).Nomenclatura Dinâmica de Ferramentas: Os nomes das ferramentas podem se adaptar dinamicamente ao contexto. Por exemplo, ao usar a skill em um repositório como facebook/react, a ferramenta assume automaticamente o nome fetch\_react\_documentation \[Source: 4: read-github by am-will/codex-skills\] .Fluxo de Trabalho (Workflow): Uma estrutura lógica de etapas recomendadas para que o agente utilize as ferramentas de forma eficiente. O fluxo estruturado para a skill do GitHub, por exemplo, determina que o agente deve \[Source: 5: read-github by am-will/codex-skills\] :Buscar a documentação primeiro para entender o projeto.Usar a busca em documentos para tirar dúvidas de uso ou recursos.Usar a busca de código para encontrar implementações específicas.Buscar URLs externas referenciadas na documentação.

