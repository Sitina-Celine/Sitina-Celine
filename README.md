<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a1a1c,55:0f3d3e,100:1f7a75&height=220&section=header&text=Celine%20Sitina&fontSize=60&fontColor=e9c46a&animation=fadeIn&fontAlignY=36&desc=Full-Stack%20Data%20Engineer%20%7C%20Data%20Integrity%2C%20Governance%20and%20Security&descSize=17&descAlignY=56" alt="Celine Sitina banner" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1400&color=2DD4BF&center=true&vCenter=true&width=720&lines=%3E+SELECT+%2A+FROM+engineers+WHERE+name+%3D+%27Celine%27;%3E+role%3A+Full-Stack+Data+Engineer;%3E+focus%3A+how+systems+work+and+move+data;%3E+cares_about%3A+integrity%2C+governance%2C+security;%3E+builds_with%3A+Python%2C+SQL%2C+Databricks%2C+dbt;%3E+1+row+returned+from+Nairobi%2C+Kenya" alt="SQL terminal typing animation" />
</p>

## About me

I'm a full-stack data engineer in Nairobi. I care about the whole journey data takes through a system: where it comes from, how it moves, how it changes along the way, and whether it can still be trusted when it arrives. Here's me, as a query:

```sql
SELECT role, focus, cares_about, community
FROM engineers
WHERE name = 'Celine Sitina'
  AND location = 'Nairobi, Kenya';
```

| role | focus | cares_about | community |
|---|---|---|---|
| Full-Stack Data Engineer | How systems work and move data, end to end | Data integrity, governance, and security | DAMA Kenya (Data Management Association) |

<sub>1 row returned. 0 rows failed validation.</sub>

### What I stand for

| Principle | What it means in my work |
|---|---|
| **Integrity** | Data should be as correct when it lands as when it left the source. Every pipeline should check its own data, not just move it. |
| **Governance** | Data needs clear ownership, definitions, and lineage, so people know where a number came from and can trust it. This is why I'm part of DAMA. |
| **Security** | Access to data should be deliberate. The right people see the right data, and sensitive data is protected at every stage. |

## How I work with data

```mermaid
flowchart LR
    subgraph COLLECT[" Collect "]
        A[(Sources<br/>APIs, files,<br/>finance data)]
        B[/Ingest<br/>Python, SQL/]
    end

    subgraph PROCESS[" Process "]
        V[Validate<br/>quality checks<br/>and tests]
        C[[Transform and model<br/>Databricks, dbt]]
    end

    subgraph SERVE[" Serve "]
        D{{Analytics<br/>Power BI}}
        E{{Applications<br/>APIs, web apps}}
        F{{AI and ML}}
    end

    G[/Govern and secure<br/>lineage, ownership,<br/>access control\]

    A ==> B ==> V ==> C
    C ==> D
    C ==> E
    C ==> F

    G -.- B
    G -.- V
    G -.- C

    classDef source fill:#0a1a1c,stroke:#2dd4bf,stroke-width:1.5px,color:#e6f4f1
    classDef pipe fill:#0f3d3e,stroke:#2dd4bf,stroke-width:1.5px,color:#e6f4f1
    classDef output fill:#1f7a75,stroke:#2dd4bf,stroke-width:1.5px,color:#ffffff
    classDef accent fill:#e9c46a,stroke:#ffffff,stroke-width:1.5px,color:#0a1a1c
    classDef group fill:transparent,stroke:#0f3d3e,stroke-width:1px,color:#e9c46a

    class A source
    class B,V,C pipe
    class D,E,F output
    class G accent
    class COLLECT,PROCESS,SERVE group

    linkStyle default stroke:#2dd4bf,stroke-width:2px
```

<sub>Data moves left to right. Governance and security are not a final step: they watch every stage along the way.</sub>

## Tech stack

<table>
  <tr>
    <th>1. Ingest</th>
    <th>2. Transform and model</th>
    <th>3. Govern and secure</th>
    <th>4. Serve</th>
    <th>5. Deliver through apps</th>
  </tr>
  <tr>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Python-0f3d3e?style=flat-square&logo=python&logoColor=2dd4bf" alt="Python" /><br/>
      <img src="https://img.shields.io/badge/SQL-0f3d3e?style=flat-square&logo=postgresql&logoColor=2dd4bf" alt="SQL" /><br/>
      <img src="https://img.shields.io/badge/REST_APIs-0f3d3e?style=flat-square" alt="REST APIs" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Databricks-0f3d3e?style=flat-square&logo=databricks&logoColor=2dd4bf" alt="Databricks" /><br/>
      <img src="https://img.shields.io/badge/dbt-0f3d3e?style=flat-square&logo=dbt&logoColor=2dd4bf" alt="dbt" /><br/>
      <img src="https://img.shields.io/badge/Data_modelling-0f3d3e?style=flat-square" alt="Data modelling" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Data_quality-9a7b2f?style=flat-square" alt="Data quality" /><br/>
      <img src="https://img.shields.io/badge/Data_governance-9a7b2f?style=flat-square" alt="Data governance" /><br/>
      <img src="https://img.shields.io/badge/Data_security-9a7b2f?style=flat-square" alt="Data security" /><br/>
      <img src="https://img.shields.io/badge/dbt_tests-9a7b2f?style=flat-square&logo=dbt&logoColor=ffffff" alt="dbt tests" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Power_BI-0f3d3e?style=flat-square&logo=powerbi&logoColor=2dd4bf" alt="Power BI" /><br/>
      <img src="https://img.shields.io/badge/DAX-0f3d3e?style=flat-square" alt="DAX" /><br/>
      <img src="https://img.shields.io/badge/Jupyter-0f3d3e?style=flat-square&logo=jupyter&logoColor=2dd4bf" alt="Jupyter" /><br/>
      <img src="https://img.shields.io/badge/scikit--learn-0f3d3e?style=flat-square&logo=scikitlearn&logoColor=2dd4bf" alt="scikit-learn" />
    </td>
    <td valign="top" align="center">
      <img src="https://img.shields.io/badge/Django-0f3d3e?style=flat-square&logo=django&logoColor=2dd4bf" alt="Django" /><br/>
      <img src="https://img.shields.io/badge/Spring_Boot-0f3d3e?style=flat-square&logo=springboot&logoColor=2dd4bf" alt="Spring Boot" /><br/>
      <img src="https://img.shields.io/badge/React-0f3d3e?style=flat-square&logo=react&logoColor=2dd4bf" alt="React" /><br/>
      <img src="https://img.shields.io/badge/TypeScript-0f3d3e?style=flat-square&logo=typescript&logoColor=2dd4bf" alt="TypeScript" />
    </td>
  </tr>
  <tr>
    <td colspan="5" align="center">
      <sub>Running underneath it all</sub><br/>
      <img src="https://img.shields.io/badge/Docker-0a1a1c?style=flat-square&logo=docker&logoColor=e9c46a" alt="Docker" />
      <img src="https://img.shields.io/badge/Git-0a1a1c?style=flat-square&logo=git&logoColor=e9c46a" alt="Git" />
      <img src="https://img.shields.io/badge/GitHub_Actions-0a1a1c?style=flat-square&logo=githubactions&logoColor=e9c46a" alt="GitHub Actions" />
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
      <p>End-to-end pipeline that ingests Formula 1 data from the Ergast API, cleans and models it into analysis-ready tables, and keeps the data consistent from source to output.</p>
      <img src="https://img.shields.io/badge/Python-0f3d3e?style=flat-square" alt="Python" />
      <img src="https://img.shields.io/badge/SQL-0f3d3e?style=flat-square" alt="SQL" />
      <img src="https://img.shields.io/badge/Databricks-0f3d3e?style=flat-square" alt="Databricks" />
      <img src="https://img.shields.io/badge/type-data_engineering-9a7b2f?style=flat-square&labelColor=0f3d3e" alt="Data engineering" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-FINANCE-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0f3d3e,100:1f7a75&height=70&text=Finance%20Insights&fontSize=24&fontColor=e6f4f1&fontAlignY=55" alt="Finance Insights" />
      </a>
      <p>Takes messy general ledger data and cleans it in Databricks so the finance numbers can be trusted, then serves it to a Power BI dashboard with DAX measures.</p>
      <img src="https://img.shields.io/badge/Databricks-0f3d3e?style=flat-square" alt="Databricks" />
      <img src="https://img.shields.io/badge/Power_BI-0f3d3e?style=flat-square" alt="Power BI" />
      <img src="https://img.shields.io/badge/DAX-0f3d3e?style=flat-square" alt="DAX" />
      <img src="https://img.shields.io/badge/type-data_quality-9a7b2f?style=flat-square&labelColor=0f3d3e" alt="Data quality" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/Sitina-Celine">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f7a75,100:0a1a1c&height=70&text=Self-Updating%20Profile&fontSize=24&fontColor=e6f4f1&fontAlignY=55" alt="Self-Updating Profile" />
      </a>
      <p>A scheduled ETL job that runs this profile. It extracts the latest F1 result from an API, transforms it with Python, and loads it here every week. If the source fails, it keeps the last good result instead of loading bad data.</p>
      <img src="https://img.shields.io/badge/Python-0f3d3e?style=flat-square" alt="Python" />
      <img src="https://img.shields.io/badge/GitHub_Actions-0f3d3e?style=flat-square" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/REST_API-0f3d3e?style=flat-square" alt="REST API" />
      <img src="https://img.shields.io/badge/status-live-e9c46a?style=flat-square&labelColor=0f3d3e" alt="Live" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-UKILI-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f7a75,100:0f3d3e&height=70&text=UKILI%20Storefront&fontSize=24&fontColor=e6f4f1&fontAlignY=55" alt="UKILI Storefront" />
      </a>
      <p>A storefront where product, cart, and checkout data flows from Shopify's backend into a React front end, with Builder.io managing the page content.</p>
      <img src="https://img.shields.io/badge/Shopify-0f3d3e?style=flat-square" alt="Shopify" />
      <img src="https://img.shields.io/badge/React-0f3d3e?style=flat-square" alt="React" />
      <img src="https://img.shields.io/badge/TypeScript-0f3d3e?style=flat-square" alt="TypeScript" />
      <img src="https://img.shields.io/badge/Builder.io-0f3d3e?style=flat-square" alt="Builder.io" />
      <img src="https://img.shields.io/badge/type-data_integration-9a7b2f?style=flat-square&labelColor=0f3d3e" alt="Data integration" />
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
validate  : skip the load if the source returns nothing
transform : Python  (top 3 finishers to Markdown)
load      : this README, between two hidden markers
on failure: keep last good result, never load bad data
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
  <img src="https://streak-stats.demolab.com?user=Sitina-Celine&background=0a1a1c&border=0f3d3e&stroke=0f3d3e&ring=2dd4bf&fire=e9c46a&currStreakLabel=e9c46a&sideLabels=e6f4f1&currStreakNum=e6f4f1&sideNums=e6f4f1&dates=8fb8b3" alt="Contribution streak" />
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
      - name: data
        tests:
          - not_null
          - accepted_values:
              values: ["validated", "governed", "secured"]
      - name: every_number
        tests:
          - relationships:
              to: ref('trusted_source')
```

</details>

## Let's connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0f3d3e?style=flat-square)](REPLACE-WITH-YOUR-LINKEDIN-URL)
[![Portfolio](https://img.shields.io/badge/Portfolio-0f3d3e?style=flat-square)](REPLACE-WITH-YOUR-PORTFOLIO-URL)

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f7a75,45:0f3d3e,100:0a1a1c&height=120&section=footer" alt="Footer wave" />
</p>
