<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a1a1c,55:0f3d3e,100:1f7a75&height=220&section=header&text=Celine%20Sitina&fontSize=60&fontColor=e6f4f1&animation=fadeIn&fontAlignY=36&desc=Data%20Engineer%20%7C%20Full-Stack%20Builder%20%7C%20AI%2FML&descSize=18&descAlignY=56" alt="Celine Sitina banner" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1400&color=2DD4BF&center=true&vCenter=true&width=700&lines=%3E+SELECT+%2A+FROM+engineers+WHERE+name+%3D+%27Celine%27;%3E+role%3A+Data+Engineer+and+Full-Stack+Builder;%3E+stack%3A+Databricks%2C+dbt%2C+Power+BI%2C+Python;%3E+also+builds%3A+React%2C+Django%2C+Spring+Boot;%3E+exploring%3A+AI+and+machine+learning;%3E+1+row+returned+from+Nairobi%2C+Kenya" alt="SQL terminal typing animation" />
</p>

## About me

I'm a data engineer in Nairobi who also builds full-stack apps. Here's me, as a query:

```sql
SELECT role, focus, currently_building, currently_learning, community
FROM engineers
WHERE name = 'Celine Sitina'
  AND location = 'Nairobi, Kenya';
```

| role | focus | currently_building | currently_learning | community |
|---|---|---|---|---|
| Data Engineer and Full-Stack Builder | Data platforms, analytics engineering, AI/ML | UKILI, a React storefront on Shopify | Builder.io | DAMA Kenya |

<sub>1 row returned. Query time: a lifetime of curiosity.</sub>

## How I work with data

```mermaid
flowchart LR
    subgraph IN[" Collect "]
        A[(Sources<br/>APIs, files,<br/>finance data)]
        B[/Ingest<br/>Python/]
    end

    subgraph PROC[" Process "]
        C[[Transform<br/>Databricks, dbt, SQL]]
    end

    subgraph OUT[" Deliver "]
        D{{Analyse<br/>Power BI, DAX}}
        E{{Build<br/>React, Django,<br/>Spring Boot}}
        F{{Explore<br/>AI and ML}}
    end

    A ==> B ==> C
    C ==> D
    C ==> E
    C ==> F

    classDef source fill:#0a1a1c,stroke:#2dd4bf,stroke-width:1.5px,color:#e6f4f1
    classDef pipe fill:#0f3d3e,stroke:#2dd4bf,stroke-width:1.5px,color:#e6f4f1
    classDef output fill:#1f7a75,stroke:#2dd4bf,stroke-width:1.5px,color:#ffffff
    classDef accent fill:#f472b6,stroke:#ffffff,stroke-width:1.5px,color:#0a1a1c
    classDef group fill:transparent,stroke:#0f3d3e,stroke-width:1px,color:#2dd4bf

    class A source
    class B,C pipe
    class D,E output
    class F accent
    class IN,PROC,OUT group

    linkStyle default stroke:#2dd4bf,stroke-width:2px
```

## Tech stack

<table>
  <tr>
    <th>1. Ingest</th>
    <th>2. Transform</th>
    <th>3. Analyse</th>
    <th>4. Build</th>
    <th>5. Explore</th>
  </tr>
  <tr>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Python-0f3d3e?style=flat-square&logo=python&logoColor=2dd4bf" alt="Python" /><br/>
      <img src="https://img.shields.io/badge/SQL-0f3d3e?style=flat-square&logo=postgresql&logoColor=2dd4bf" alt="SQL" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Databricks-0f3d3e?style=flat-square&logo=databricks&logoColor=2dd4bf" alt="Databricks" /><br/>
      <img src="https://img.shields.io/badge/dbt-0f3d3e?style=flat-square&logo=dbt&logoColor=2dd4bf" alt="dbt" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Power_BI-0f3d3e?style=flat-square&logo=powerbi&logoColor=2dd4bf" alt="Power BI" /><br/>
      <img src="https://img.shields.io/badge/DAX-0f3d3e?style=flat-square" alt="DAX" /><br/>
      <img src="https://img.shields.io/badge/Jupyter-0f3d3e?style=flat-square&logo=jupyter&logoColor=2dd4bf" alt="Jupyter" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/React-0f3d3e?style=flat-square&logo=react&logoColor=2dd4bf" alt="React" /><br/>
      <img src="https://img.shields.io/badge/TypeScript-0f3d3e?style=flat-square&logo=typescript&logoColor=2dd4bf" alt="TypeScript" /><br/>
      <img src="https://img.shields.io/badge/Vite-0f3d3e?style=flat-square&logo=vite&logoColor=2dd4bf" alt="Vite" /><br/>
      <img src="https://img.shields.io/badge/Django-0f3d3e?style=flat-square&logo=django&logoColor=2dd4bf" alt="Django" /><br/>
      <img src="https://img.shields.io/badge/Spring_Boot-0f3d3e?style=flat-square&logo=springboot&logoColor=2dd4bf" alt="Spring Boot" /><br/>
      <img src="https://img.shields.io/badge/Shopify-0f3d3e?style=flat-square&logo=shopify&logoColor=2dd4bf" alt="Shopify" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/scikit--learn-0f3d3e?style=flat-square&logo=scikitlearn&logoColor=2dd4bf" alt="scikit-learn" />
    </td>
  </tr>
  <tr>
    <td colspan="5" align="center">
      <sub>Running underneath it all</sub><br/>
      <img src="https://img.shields.io/badge/Docker-0a1a1c?style=flat-square&logo=docker&logoColor=2dd4bf" alt="Docker" />
      <img src="https://img.shields.io/badge/Git-0a1a1c?style=flat-square&logo=git&logoColor=2dd4bf" alt="Git" />
      <img src="https://img.shields.io/badge/GitHub_Actions-0a1a1c?style=flat-square&logo=githubactions&logoColor=2dd4bf" alt="GitHub Actions" />
    </td>
  </tr>
</table>

## Featured projects

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-F1-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0a1a1c,100:1f7a75&height=70&text=F1%20Data%20Pipeline&fontSize=24&fontColor=e6f4f1&fontAlignY=55" alt="F1 Data Pipeline" />
      </a>
      <p>End-to-end pipeline that pulls Formula 1 data from the Ergast API, cleans and models it, and makes it ready for analysis.</p>
      <img src="https://img.shields.io/badge/Python-0f3d3e?style=flat-square" alt="Python" />
      <img src="https://img.shields.io/badge/SQL-0f3d3e?style=flat-square" alt="SQL" />
      <img src="https://img.shields.io/badge/Databricks-0f3d3e?style=flat-square" alt="Databricks" />
      <img src="https://img.shields.io/badge/type-data_engineering-1f7a75?style=flat-square&labelColor=0f3d3e" alt="Data engineering" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-FINANCE-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0f3d3e,100:1f7a75&height=70&text=Finance%20Insights&fontSize=24&fontColor=e6f4f1&fontAlignY=55" alt="Finance Insights" />
      </a>
      <p>Cleans raw general ledger data in Databricks and turns it into a Power BI finance dashboard with DAX measures.</p>
      <img src="https://img.shields.io/badge/Databricks-0f3d3e?style=flat-square" alt="Databricks" />
      <img src="https://img.shields.io/badge/Power_BI-0f3d3e?style=flat-square" alt="Power BI" />
      <img src="https://img.shields.io/badge/DAX-0f3d3e?style=flat-square" alt="DAX" />
      <img src="https://img.shields.io/badge/type-analytics-1f7a75?style=flat-square&labelColor=0f3d3e" alt="Analytics" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-UKILI-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f7a75,100:0f3d3e&height=70&text=UKILI%20Storefront&fontSize=24&fontColor=e6f4f1&fontAlignY=55" alt="UKILI Storefront" />
      </a>
      <p>E-commerce storefront where a React app uses Shopify as its backend for products, cart, and checkout, with Builder.io for visual page editing.</p>
      <img src="https://img.shields.io/badge/React-0f3d3e?style=flat-square" alt="React" />
      <img src="https://img.shields.io/badge/TypeScript-0f3d3e?style=flat-square" alt="TypeScript" />
      <img src="https://img.shields.io/badge/Shopify-0f3d3e?style=flat-square" alt="Shopify" />
      <img src="https://img.shields.io/badge/Builder.io-0f3d3e?style=flat-square" alt="Builder.io" />
      <img src="https://img.shields.io/badge/type-frontend-1f7a75?style=flat-square&labelColor=0f3d3e" alt="Frontend" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/Sitina-Celine">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f7a75,100:0a1a1c&height=70&text=Self-Updating%20Profile&fontSize=24&fontColor=e6f4f1&fontAlignY=55" alt="Self-Updating Profile" />
      </a>
      <p>This profile runs its own scheduled ETL job: GitHub Actions extracts the latest F1 race result from an API, transforms it with Python, and loads it into this page every week.</p>
      <img src="https://img.shields.io/badge/Python-0f3d3e?style=flat-square" alt="Python" />
      <img src="https://img.shields.io/badge/GitHub_Actions-0f3d3e?style=flat-square" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/REST_API-0f3d3e?style=flat-square" alt="REST API" />
      <img src="https://img.shields.io/badge/status-live-f472b6?style=flat-square&labelColor=0f3d3e" alt="Live" />
    </td>
  </tr>
</table>

## Live from my data pipeline

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/Sitina-Celine/Sitina-Celine/f1.yml?style=flat-square&label=F1%20ETL%20job&labelColor=0f3d3e" alt="F1 ETL job status" />
  <img src="https://img.shields.io/github/actions/workflow/status/Sitina-Celine/Sitina-Celine/profile-3d.yml?style=flat-square&label=3D%20city%20job&labelColor=0f3d3e" alt="3D city job status" />
  <img src="https://img.shields.io/github/actions/workflow/status/Sitina-Celine/Sitina-Celine/snake.yml?style=flat-square&label=Snake%20job&labelColor=0f3d3e" alt="Snake job status" />
</p>

```text
schedule  : every Monday, 06:00 UTC
extract   : Jolpica F1 API  (latest race)
transform : Python  (top 3 finishers to Markdown)
load      : this README, between two hidden markers
on failure: keep last good result, never break the page
```

[See the pipeline code](scripts/update_f1.py)

<!-- F1:START -->

**Brazilian Grand Prix** (season 2026, round 20, 2026-11-08)

| Pos | Driver | Team | Time / Status |
| --- | --- | --- | --- |
| 1 | Lando Norris | McLaren | 1:35:23.504 |
| 2 | Max Verstappen | Red Bull | +14.602 |
| 3 | Isack Hadjar | Red Bull | +24.485 |

<sub>Pipeline last ran: 2026-11-14 20:48 UTC. Source: Jolpica F1 API.</sub>

<!-- F1:END -->

## GitHub activity

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Sitina-Celine&background=0a1a1c&border=0f3d3e&stroke=0f3d3e&ring=2dd4bf&fire=f472b6&currStreakLabel=2dd4bf&sideLabels=e6f4f1&currStreakNum=e6f4f1&sideNums=e6f4f1&dates=8fb8b3" alt="Contribution streak" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Sitina-Celine/Sitina-Celine/output-3d/profile-night-green.svg" alt="3D contribution city" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sitina-Celine/Sitina-Celine/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Sitina-Celine/Sitina-Celine/output/github-snake-light.svg" />
    <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/Sitina-Celine/Sitina-Celine/output/github-snake-dark.svg" />
  </picture>
</p>

<details>
  <summary><b>Click here if you're a data engineer</b></summary>

```yaml
# Data quality tests that run on me every day
models:
  - name: celine_sitina
    columns:
      - name: curiosity
        tests:
          - not_null
      - name: approach
        tests:
          - unique
      - name: problems
        tests:
          - accepted_values:
              values: ["solved", "being_solved"]
      - name: data
        tests:
          - relationships:
              to: ref('decisions')
```

</details>

## Let's connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0f3d3e?style=flat-square)](REPLACE-WITH-YOUR-LINKEDIN-URL)
[![Portfolio](https://img.shields.io/badge/Portfolio-0f3d3e?style=flat-square)](REPLACE-WITH-YOUR-PORTFOLIO-URL)

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f7a75,45:0f3d3e,100:0a1a1c&height=120&section=footer" alt="Footer wave" />
</p>
