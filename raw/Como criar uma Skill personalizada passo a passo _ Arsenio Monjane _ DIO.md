---
sourceFile: "Como criar uma Skill personalizada passo a passo | Arsenio Monjane | DIO"
exportedBy: "Kortex"
exportDate: "2026-05-17T23:05:02.669Z"
---

# Como criar uma Skill personalizada passo a passo | Arsenio Monjane | DIO

465495db-4c30-4279-9d16-9426453cabb5

Como criar uma Skill personalizada passo a passo | Arsenio Monjane | DIO

be1f56ea-f774-4717-a214-2e6a87f7ec2c

https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf

Como criar uma Skill personalizada passo a passo | Arsenio Monjane | DIO

MATRICULE-SE

https://www.dio.me/

https://www.dio.me/bootcamp

https://www.dio.me/projects

https://www.dio.me/articles

https://www.dio.me/planos

Para Empresas

https://www.dio.me/talent-match

https://www.dio.me/sign-in

Criar conta

https://www.dio.me/sign-up

Lista de conteúdos

https://www.dio.me/articles

Arsenio Monjane 02/04/2026 05:16

Compartilhe

https://www.linkedin.com/shareArticle?mini=true&url=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf?q=1289

https://facebook.com/sharer/sharer.php?u=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf

https://twitter.com/share?&text=Como%20criar%20uma%20Skill%20personalizada%20passo%20a%20passo&url=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf

https://api.whatsapp.com/send?text=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf

\[\](mailto:?body=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf&subject=Como criar uma Skill personalizada passo a passo)

Como criar uma Skill personalizada passo a passo

Com o avanço das plataformas de IA de agentes, como o Antigravity, surgem formas mais estruturadas e reutilizáveis de orientar o comportamento do modelo, por meio do conceito de

. Uma skill é, em essência, um módulo de instruções especializado que define claramente o que o agente deve fazer em determinado contexto, com regras, exemplos e, opcionalmente, scripts de automação (Hora de Codar, 2026; Google Antigravity Documentation, 2026).

Esse tipo de abstração permite padronizar processos técnicos (como formatação de commits, geração de boilerplate, revisão de código e segurança) sem depender exclusivamente de prompts espontâneos, tornando o trabalho com IA mais previsível e auditável (Google Antigravity, 2026; Compilatio, 2026).

Como criar uma skill personalizada passo a passo

Para criar uma

skill personalizada no Antigravity

, você precisa definir uma pasta, um arquivo SKILL.md com metadados em YAML e instruções claras, e, opcionalmente, scripts de automação (por exemplo, em Python ou Bash) que o agente poderá executar quando necessário (Antigravity Skills, 2026; Google Antigravity Documentation, 2026).

1. Planeje o que a skill deve fazer

Antes de codificar, defina com precisão

qual tarefa a skill deve automatizar

, por exemplo: “formatar commits seguindo o padrão do projeto”, “gerar boilerplate de API REST em Flask” ou “revisar código de segurança” (Hora de Codar, 2026; Google Antigravity Documentation, 2026).

o que entra (entrada, como um diff de commit ou código‑fonte);

o que sai (saída esperada, ex.: mensagem de commit formatada ou arquivo de teste já pronto).

2. Crie a estrutura de pasta da skill

No seu projeto / workspace, organize a estrutura conforme o padrão aberto de skills do Antigravity (Google Antigravity Documentation, 2026; Hora de Codar, 2026):

.seu-projeto/

├── .agent/

│  └── skills/

│      └── minha-skill-nova/     # nome da pasta da skill

│          ├── SKILL.md

│          ├── scripts/          # opcional

│          │  └── run.py

│          └── references/       # opcional

O Antigravity espera que cada skill seja uma pasta com um arquivo SKILL.md principal, que contém as instruções e metadados para que o roteador de skills a reconheça e ative em contexto adequado (Google Antigravity Documentation, 2026; Compilatio, 2026).

3. Defina o SKILL.md com frontmatter YAML

No SKILL.md, use o formato

frontmatter YAML + conteúdo em Markdown

, como recomendado na documentação oficial do Antigravity (Google Antigravity Documentation, 2026; Hora de Codar, 2026):

#### Exemplo de cabeçalho:

---

name: "FormatarCommitFlask"

description: "Skill que formata commits seguindo o padrão esperado em projetos Flask deste projeto."

scope: "workspace"

commands:

 - "formatar commit"

 - "padronizar commit"

author: "SeuNome"

version: "1.0.0"

---

A seção description é especialmente importante: ela atua como “frase‑ativação” que o LLM usa para decidir se deve carregar essa skill (Google Antigravity Documentation, 2026).

#### Corpo do SKILL.md (suas instruções):

### Meta

- Objetivo: padronizar mensagens de commit para o projeto Flask.

- Quem usa: devs do backend.

 

### Entrada

- Diff do commit ou descrição bruta do que foi feito.

 

### Saída esperada

- Mensagem de commit em formato:

 \`tipo(scope): descrição curta em até 50 caracteres\`

 + 1 linha vazia

 + corpo explicativo em português (se a mudança for complexa).

 

### Regras

- tipos possíveis: \`feat\`, \`fix\`, \`refactor\`, \`docs\`, \`test\`, \`chore\`.

- \`scope\` deve ser o nome do módulo (ex.: \`api\`, \`auth\`, \`db\`).

- Proibido usar acento em inglês; se usar português, manter termos claros.

- Não usar imperativo em inglês; usar terceira pessoa em português no corpo.

O corpo do Markdown deve conter

objetivo, instruções detalhadas, exemplos de entrada e saída e restrições

(“não faça isso”) para guiar o comportamento do agente (Google Antigravity Documentation, 2026).

4. (Opcional) Adicione scripts de automação

Para skills mais avançadas, o Antigravity permite scripts em linguagens populares (por exemplo, Python ou JavaScript) que o agente invoca quando necessário (Hora de Codar, 2026; Google Antigravity Documentation, 2026).

Crie scripts em scripts/ (ex.: scripts/run.py ou scripts/util.sh).

#### No SKILL.md, descreva claramente como o agente deve usá‑los, por exemplo:

### Execução

- O agente deve chamar \`scripts/run.py\` passando o diff via stdin.

- Verificar o código de retorno; se for ≠ 0, retornar o erro formatado.

Isso aumenta a confiabilidade da skill, pois parte da lógica pesada é executada em código nativo, não apenas em texto gerado por IA (Google Antigravity Documentation, 2026).

5. Defina o escopo: global ou workspace

Segundo a documentação do Antigravity, skills podem ser definidas em escopo

(disponível em todos os workspaces) ou

(local ao projeto atual) (Google Antigravity Documentation, 2026; Hora de Codar, 2026).

Escopo global

: útil para regras gerais (ex.: padrão de commits, boas‑práticas de segurança, licenças).

Escopo workspace

: mais adequado para regras específicas de um projeto (ex.: arquitetura de API, padrão de banco de dados).

Você configura esse escopo no frontmatter YAML ou na documentação da pasta, dependendo da configuração do seu ambiente (Google Antigravity Documentation, 2026).

6. Teste a skill em contexto real

Antes de reutilizar amplamente, teste a skill com entradas reais do seu projeto (Hora de Codar, 2026; Google Antigravity Documentation, 2026):

#### Peça ao agente:

executar um comando condizente com os commands da skill (ex.: “formatar commit”);

verificar se o formato e as regras estão sendo seguidas.

Ajuste o SKILL.md até que o comportamento seja consistente, adicionando exemplos reais como demonstração de uso.

7. Compartilhe ou reutilize a skill

Se a skill for útil em múltiplos projetos, torne o escopo

e mova a pasta para a localização de skills globais do Antigravity (Google Antigravity Documentation, 2026; Hora de Codar, 2026).Você também pode compartilhar a pasta completa em repositórios públicos (ex.: GitHub, “Antigravity Kit”) para que outros desenvolvedores a utilizem ou adaptem (Hora de Codar, 2026; Google Antigravity Documentation, 2026).

Agora que você conhece o passo a passo para criar uma

skill personalizada no Antigravity

, o próximo passo é

colocar isso em prática no seu próprio projeto

. Escolha uma tarefa repetitiva do seu fluxo de trabalho (por exemplo, formatação de commits, criação de testes-unitários ou revisão de segurança) e mapeie os critérios em um SKILL.md dentro da pasta .agent/skills/.

Depois de testar a skill em um ou dois cenários reais, compartilhe o modelo com sua equipe ou repositório pessoal, transformando esse conhecimento em um ativo reutilizável e evolutivo para futuras integrações com IA no desenvolvimento de software.

A criação de skills personalizadas no Antigravity representa uma evolução prática na forma de integrar IA ao fluxo de trabalho de desenvolvimento, permitindo transformar conhecimento técnico e padrões internos em módulos reutilizáveis e auditáveis (Hora de Codar, 2026; Google Antigravity Documentation, 2026).

Ao seguir um passo a passo estruturado — desde a definição clara da tarefa, passando pela organização da pasta e do SKILL.md, até a adição de scripts e testes em contexto real — você constrói skills robustas que reduzem erros manuais, padronizam processos e podem ser compartilhadas entre equipes e projetos (Google Antigravity, 2026; Mettzer, 2017).

Referências bibliográficas

Hora de Codar. (2026).

Como criar Skills personalizados no Antigravity

. https://horadecodar.com.br/criar-skills-personalizados-antigravity/

Google Antigravity. (2026).

Agent Skills – Google Antigravity Documentation

. https://antigravity.google/docs/skills

Google Antigravity. (2026).

Getting started with Antigravity Skills

(codelab). https://codelabs.developers.google.com/getting-started-with-antigravity-skills?hl=pt-br

Compartilhe

https://www.linkedin.com/shareArticle?mini=true&url=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf?q=625

https://facebook.com/sharer/sharer.php?u=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf

https://twitter.com/share?&text=Como%20criar%20uma%20Skill%20personalizada%20passo%20a%20passo&url=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf

https://api.whatsapp.com/send?text=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf

\[\](mailto:?body=https://www.dio.me/articles/como-criar-uma-skill-personalizada-passo-a-passo-12de3bf66cdf&subject=Como criar uma Skill personalizada passo a passo)

0 0 Comentar

Recomendados para você

Comentários (0)

Leia a seguir

10 Ferramentas Obrigatórias de Inteligência Artificial para Escalar Negócios 🌍 💼 📈 📊 Rafael Pereira - 15 de Maio #Workflow Automation#Integração de IA no Marketing#Youtube#Inteligência Artificial (IA)

https://www.dio.me/articles/10-ferramentas-obrigatorias-de-inteligencia-artificial-para-escalar-negocios-c996082abc84

DS CAMPUS EXPERT TURMA16 Daiana Santos - 15 de Maio

https://www.dio.me/articles/titulo-do-artigo-8505b236620c

Turma 16 DIO Campus Expert Vivien Galvao - 15 de Maio

https://www.dio.me/articles/turma-16-dio-campus-expert-91f8fb562dab

Mais informações

make the change

https://www.dio.me/planos

https://www.dio.me/bootcamp

https://www.dio.me/projects

https://www.dio.me/articles

Para Empresas

https://www.dio.me/talent-match

Depoimentos

https://www.dio.me/depoimentos

Informações

Central de Ajuda

https://help.dio.me/pt-BR/

Termos de Uso

https://www.dio.me/terms

Políticas de Privacidade

https://www.dio.me/policies

\[Canal de Contato LGPD\](mailto:lgpd%40dio.me?subject=Gostaria de Retirar uma Dúvida Sobre LGPD)

AI Agent Builder

Curso Inteligência Artificial

https://www.dio.me/curso-inteligencia-artificial

Formação CrewAI Fundamentals

https://www.dio.me/curso-crewai-do-zero

AI Automation

Curso Inteligência Artificial

https://www.dio.me/curso-inteligencia-artificial

Curso AI Automation com N8N

https://www.dio.me/curso-ai-automation-com-n8n

Formação CrewAI Fundamentals

https://www.dio.me/curso-crewai-do-zero

AI Developer

Curso Inteligência Artificial

https://www.dio.me/curso-inteligencia-artificial

Curso Chat GPT for Devs

https://www.dio.me/curso-chat-gpt-for-devs

Formação Github Copilot

https://www.dio.me/curso-github-copilot

Formação Microsoft Azure AI Fundamentals (AI-900)

https://www.dio.me/curso-ai-900

Formação AI-102 Certification

https://www.dio.me/curso-ai-102

Formação AI Builder com Lovable

https://www.dio.me/curso-ia-builder-com-lovable

AI Data Scientist

Curso Inteligência Artificial

https://www.dio.me/curso-inteligencia-artificial

Curso Machine Learning

https://www.dio.me/curso-machine-learning

Back-end Developer

Curso Java Developer

https://www.dio.me/curso-java

Curso .NET Developer

https://www.dio.me/curso-dot-net

Curso Python Fundamentals

https://www.dio.me/curso-python-do-zero

Curso TypeScript Fullstack Developer

https://www.dio.me/curso-typescript

Curso PHP Experience

https://www.dio.me/curso-php-completo

Curso Golang Developer

https://www.dio.me/curso-golang

https://www.dio.me/catalog?careerId=1b73eec2-c27b-4820-8e79-8238c93a5224

Front-end Developer

Curso HTML Developer

https://www.dio.me/curso-html

Curso CSS Developer

https://www.dio.me/curso-css

Curso JavaScript Developer

https://www.dio.me/curso-javascript

Curso Angular

https://www.dio.me/curso-angular

Curso React Developer

https://www.dio.me/curso-react

Curso TypeScript Fullstack Developer

https://www.dio.me/curso-typescript

https://www.dio.me/catalog?careerId=9f3d4f16-ef54-412e-9156-38482e2d51a3

ACADEMIA PME EDUCACAO E CONSULTORIA EM NEGOCIOS LTDA. CNPJ: 26.965.884/0001-02

