<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,55:2b1430,100:7a1a6c&height=220&section=header&text=Celine%20Sitina&fontSize=60&fontColor=ff4fd8&animation=fadeIn&fontAlignY=36&desc=Full-Stack%20Data%20Engineer%20%7C%20Systems%20%C2%B7%20Governance%20%C2%B7%20Analytics%20%C2%B7%20AI%2FML&descSize=17&descAlignY=56" alt="Celine Sitina banner" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1400&color=FF4FD8&center=true&vCenter=true&width=720&lines=%3E+SELECT+%2A+FROM+engineers+WHERE+name+%3D+%27Celine%27;%3E+role%3A+Full-Stack+Data+Engineer;%3E+core%3A+pipelines+that+move+data+and+keep+it+trustworthy;%3E+builds%3A+the+systems+the+data+flows+through;%3E+protects%3A+data+quality%2C+governance%2C+security;%3E+serves%3A+analytics+and+AI%2FML;%3E+1+row+returned+from+Nairobi%2C+Kenya" alt="SQL terminal typing animation" />
</p>

## About me

I'm a full-stack data engineer in Nairobi. My core work is building the pipelines and platforms that move data and keep it trustworthy. Around that core I build the systems the data flows through, protect its quality and governance, and serve it to analytics and AI/ML. Here's me, as a query:

```sql
SELECT data_engineering, systems, governance, analytics, ai_ml
FROM engineers
WHERE name = 'Celine Sitina'
  AND location = 'Nairobi, Kenya';
```

| data_engineering | systems | governance | analytics | ai_ml |
|---|---|---|---|---|
| Pipelines, modelling, Databricks, dbt, SQL, Python | APIs and apps with Spring Boot, Django, React | Data quality, integrity, security, DAMA Kenya member | Power BI, DAX, Jupyter | scikit-learn, model-ready data |

<sub>1 row returned. 0 rows failed validation.</sub>

<table>
  <tr>
    <td width="45%" valign="top">

```mermaid
%%{init: {'theme':'base','themeVariables':{
  'pie1':'#7a1a6c','pie2':'#2b1430','pie3':'#ff4fd8','pie4':'#f2a7e0','pie5':'#4a1f4d',
  'pieTitleTextColor':'#f3e9f3','pieSectionTextColor':'#ffffff','pieLegendTextColor':'#f3e9f3',
  'pieStrokeColor':'#0d0d0d','pieOuterStrokeColor':'#0d0d0d'}}}%%
pie showData title How my work splits
    "Data engineering" : 60
    "Software and system design" : 10
    "Data governance and quality" : 10
    "Data analytics" : 10
    "AI and ML" : 10
```

</td>
    <td width="55%" valign="top">
      <h3>What each slice means</h3>
      <p><b>Data engineering (60%)</b>: the core. Ingesting data from APIs and files, validating it, modelling and transforming it in Databricks and dbt, and running it on a schedule so it keeps working after I walk away.</p>
      <p><b>Software and system design (10%)</b>: I build the APIs and applications the data flows through, so I understand the systems on both ends of a pipeline, not just the middle.</p>
      <p><b>Data governance and quality (10%)</b>: data should be as correct when it lands as when it left the source, with clear ownership, lineage, and controlled access. This is why I'm part of DAMA Kenya.</p>
      <p><b>Data analytics (10%)</b>: shaping clean data into Power BI dashboards and DAX measures that people can act on.</p>
      <p><b>AI and ML (10%)</b>: preparing model-ready data and experimenting with machine learning on top of well-built pipelines.</p>
    </td>
  </tr>
</table>

## How I work with data

```mermaid
flowchart LR
    subgraph SYS[" Systems I build "]
        S[Applications and APIs<br/>Spring Boot, Django, React]
    end

    subgraph COLLECT[" Collect "]
        A[(Sources<br/>APIs, files,<br/>finance data)]
        B[/Ingest<br/>Python, SQL/]
    end

    subgraph PROCESS[" Process "]
        V[Validate<br/>quality checks<br/>and tests]
        C[[Transform and model<br/>Databricks, dbt]]
    end

    subgraph SERVE[" Serve "]
        D{{Analytics<br/>Power BI, DAX}}
        F{{AI and ML<br/>scikit-learn}}
    end

    G[/Govern and secure<br/>lineage, ownership,<br/>access control\]

    S ==> A
    A ==> B ==> V ==> C
    C ==> D
    C ==> F
    C ==> S

    G -.- B
    G -.- V
    G -.- C

    classDef system fill:#0d0d0d,stroke:#b58ab0,stroke-width:1.5px,color:#f3e9f3
    classDef source fill:#0d0d0d,stroke:#f2a7e0,stroke-width:1.5px,color:#f3e9f3
    classDef pipe fill:#2b1430,stroke:#f2a7e0,stroke-width:1.5px,color:#f3e9f3
    classDef output fill:#7a1a6c,stroke:#f2a7e0,stroke-width:1.5px,color:#ffffff
    classDef accent fill:#ff4fd8,stroke:#ffffff,stroke-width:1.5px,color:#0d0d0d
    classDef group fill:transparent,stroke:#2b1430,stroke-width:1px,color:#f2a7e0

    class S system
    class A source
    class B,V,C pipe
    class D,F output
    class G accent
    class SYS,COLLECT,PROCESS,SERVE group

    linkStyle default stroke:#f2a7e0,stroke-width:2px
```

<sub>The applications I build both produce data for the pipeline and consume what comes out of it. Governance and security watch every stage in between.</sub>

## Tech stack

<table>
  <tr>
    <th colspan="2">Data engineering</th>
    <th>Software and systems</th>
    <th>Governance and quality</th>
    <th>Analytics</th>
    <th>AI and ML</th>
  </tr>
  <tr>
    <td valign="top" align="center">
      <sub>Ingest</sub><br/>
      <img src="https://img.shields.io/badge/Python-2b1430?style=flat-square&logo=python&logoColor=f2a7e0" alt="Python" /><br/>
      <img src="https://img.shields.io/badge/SQL-2b1430?style=flat-square&logo=postgresql&logoColor=f2a7e0" alt="SQL" /><br/>
      <img src="https://img.shields.io/badge/REST_APIs-2b1430?style=flat-square" alt="REST APIs" /><br/>
      <img src="https://img.shields.io/badge/GitHub_Actions-2b1430?style=flat-square&logo=githubactions&logoColor=f2a7e0" alt="GitHub Actions" />
    </td>
    <td valign="top" align="center">
      <sub>Transform and model</sub><br/>
      <img src="https://img.shields.io/badge/Databricks-2b1430?style=flat-square&logo=databricks&logoColor=f2a7e0" alt="Databricks" /><br/>
      <img src="https://img.shields.io/badge/dbt-2b1430?style=flat-square&logo=dbt&logoColor=f2a7e0" alt="dbt" /><br/>
      <img src="https://img.shields.io/badge/Data_modelling-2b1430?style=flat-square" alt="Data modelling" /><br/>
      <img src="https://img.shields.io/badge/Docker-2b1430?style=flat-square&logo=docker&logoColor=f2a7e0" alt="Docker" />
    </td>
    <td valign="top" align="center">
      <br/>
      <img src="https://img.shields.io/badge/Spring_Boot-2b1430?style=flat-square&logo=springboot&logoColor=b58ab0" alt="Spring Boot" /><br/>
      <img src="https://img.shields.io/badge/Django-2b1430?style=flat-square&logo=django&logoColor=b58ab0" alt="Django" /><br/>
      <img src="https://img.shields.io/badge/React-2b1430?style=flat-square&logo=react&logoColor=b58ab0" alt="React" /><br/>
      <img src="https://img.shields.io/badge/TypeScript-2b1430?style=flat-square&logo=typescript&logoColor=b58ab0" alt="TypeScript" />
    </td>
    <td valign="top" align="center">
      <br/>
      <img src="https://img.shields.io/badge/Data_quality-7a1a6c?style=flat-square" alt="Data quality" /><br/>
      <img src="https://img.shields.io/badge/Data_governance-7a1a6c?style=flat-square" alt="Data governance" /><br/>
      <img src="https://img.shields.io/badge/Data_security-7a1a6c?style=flat-square" alt="Data security" /><br/>
      <img src="https://img.shields.io/badge/dbt_tests-7a1a6c?style=flat-square&logo=dbt&logoColor=ffffff" alt="dbt tests" />
    </td>
    <td valign="top" align="center">
      <br/>
      <img src="https://img.shields.io/badge/Power_BI-2b1430?style=flat-square&logo=powerbi&logoColor=f2a7e0" alt="Power BI" /><br/>
      <img src="https://img.shields.io/badge/DAX-2b1430?style=flat-square" alt="DAX" /><br/>
      <img src="https://img.shields.io/badge/Jupyter-2b1430?style=flat-square&logo=jupyter&logoColor=f2a7e0" alt="Jupyter" />
    </td>
    <td valign="top" align="center">
      <br/>
      <img src="https://img.shields.io/badge/scikit--learn-2b1430?style=flat-square&logo=scikitlearn&logoColor=f2a7e0" alt="scikit-learn" /><br/>
      <img src="https://img.shields.io/badge/pandas-2b1430?style=flat-square&logo=pandas&logoColor=f2a7e0" alt="pandas" /><br/>
      <img src="https://img.shields.io/badge/Feature_prep-2b1430?style=flat-square" alt="Feature preparation" />
    </td>
  </tr>
</table>

## Featured projects

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-F1-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0d0d0d,100:7a1a6c&height=70&text=F1%20Data%20Pipeline&fontSize=24&fontColor=f3e9f3&fontAlignY=55" alt="F1 Data Pipeline" />
      </a>
      <p>End-to-end pipeline that ingests Formula 1 data from the Ergast API, cleans and models it into analysis-ready tables, and keeps the data consistent from source to output.</p>
      <img src="https://img.shields.io/badge/Python-2b1430?style=flat-square" alt="Python" />
      <img src="https://img.shields.io/badge/SQL-2b1430?style=flat-square" alt="SQL" />
      <img src="https://img.shields.io/badge/Databricks-2b1430?style=flat-square" alt="Databricks" />
      <img src="https://img.shields.io/badge/area-data_engineering-7a1a6c?style=flat-square&labelColor=2b1430" alt="Data engineering" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-FINANCE-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:2b1430,100:7a1a6c&height=70&text=Finance%20Insights&fontSize=24&fontColor=f3e9f3&fontAlignY=55" alt="Finance Insights" />
      </a>
      <p>Takes messy general ledger data and cleans it in Databricks so the finance numbers can be trusted, then serves it to a Power BI dashboard with DAX measures.</p>
      <img src="https://img.shields.io/badge/Databricks-2b1430?style=flat-square" alt="Databricks" />
      <img src="https://img.shields.io/badge/Power_BI-2b1430?style=flat-square" alt="Power BI" />
      <img src="https://img.shields.io/badge/DAX-2b1430?style=flat-square" alt="DAX" />
      <img src="https://img.shields.io/badge/area-data_quality_and_analytics-7a1a6c?style=flat-square&labelColor=2b1430" alt="Data quality and analytics" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/Sitina-Celine">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:7a1a6c,100:0d0d0d&height=70&text=Self-Updating%20Profile&fontSize=24&fontColor=f3e9f3&fontAlignY=55" alt="Self-Updating Profile" />
      </a>
      <p>A scheduled ETL job that runs this profile. It extracts the latest F1 result from an API, transforms it with Python, and loads it here every week. If the source fails, it keeps the last good result instead of loading bad data.</p>
      <img src="https://img.shields.io/badge/Python-2b1430?style=flat-square" alt="Python" />
      <img src="https://img.shields.io/badge/GitHub_Actions-2b1430?style=flat-square" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/REST_API-2b1430?style=flat-square" alt="REST API" />
      <img src="https://img.shields.io/badge/status-live-ff4fd8?style=flat-square&labelColor=2b1430" alt="Live" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Sitina-Celine/REPLACE-UKILI-REPO">
        <img src="https://capsule-render.vercel.app/api?type=rect&color=0:7a1a6c,100:2b1430&height=70&text=UKILI%20Storefront&fontSize=24&fontColor=f3e9f3&fontAlignY=55" alt="UKILI Storefront" />
      </a>
      <p>A storefront where product, cart, and checkout data flows from Shopify's backend into a React front end, with Builder.io managing the page content. The systems side of the stack.</p>
      <img src="https://img.shields.io/badge/Shopify-2b1430?style=flat-square" alt="Shopify" />
      <img src="https://img.shields.io/badge/React-2b1430?style=flat-square" alt="React" />
      <img src="https://img.shields.io/badge/TypeScript-2b1430?style=flat-square" alt="TypeScript" />
      <img src="https://img.shields.io/badge/Builder.io-2b1430?style=flat-square" alt="Builder.io" />
      <img src="https://img.shields.io/badge/area-systems_and_integration-7a1a6c?style=flat-square&labelColor=2b1430" alt="Systems and integration" />
    </td>
  </tr>
</table>

## Live from my data pipeline

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/Sitina-Celine/Sitina-Celine/f1.yml?style=flat-square&label=F1%20ETL%20job&labelColor=2b1430" alt="F1 ETL job status" />
  <img src="https://img.shields.io/github/actions/workflow/status/Sitina-Celine/Sitina-Celine/profile-3d.yml?style=flat-square&label=3D%20city%20job&labelColor=2b1430" alt="3D city job status" />
  <img src="https://img.shields.io/github/actions/workflow/status/Sitina-Celine/Sitina-Celine/snake.yml?style=flat-square&label=Snake%20job&labelColor=2b1430" alt="Snake job status" />
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
  <img src="https://streak-stats.demolab.com?user=Sitina-Celine&background=0d0d0d&border=2b1430&stroke=2b1430&ring=f2a7e0&fire=ff4fd8&currStreakLabel=ff4fd8&sideLabels=f3e9f3&currStreakNum=f3e9f3&sideNums=f3e9f3&dates=b58ab0" alt="Contribution streak" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Sitina-Celine/Sitina-Celine/output-3d/profile-night-view.svg" alt="3D contribution city" />
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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-2b1430?style=flat-square)](REPLACE-WITH-YOUR-LINKEDIN-URL)
[![Portfolio](https://img.shields.io/badge/Portfolio-2b1430?style=flat-square)](REPLACE-WITH-YOUR-PORTFOLIO-URL)

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7a1a6c,45:2b1430,100:0d0d0d&height=120&section=footer" alt="Footer wave" />
</p>
