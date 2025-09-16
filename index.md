---
layout: about
permalink: /
title: Mario Leone
subtitle: AI Engineer & Full stack developer

profile:
  align: 
  image: FotoMarioLeone_420.jpg
  image_circular: false
  style: "width: 150px" # Rimpicciolisco la fotografia
  address: >
    <p>Lugano, Switzerland</p>

news: false
selected_papers: false
social: true
---

Experienced AI Engineer with a strong background in algorithmic trading systems and machine learning applications.

I design and implement low-latency architectures and real-time dashboards powered by intelligent trading agents. By combining C++ performance with Python-based AI models, I build solutions that enhance execution speed and decision-making in high-frequency trading environments. Beyond trading, my expertise extends to developing scalable AI systems and data-driven applications across financial and industrial domains.

---

## Skills  

### Programming Languages  

Advanced proficiency in **C++**, **Python**, and **TypeScript**, with additional experience in **R**, **MATLAB**, and **SQL**, applied across both academic research and financial/industrial contexts.  

### Artificial Intelligence / Machine Learning  

Expertise in **Large Language Models (LLMs)**, **Deep Learning**, and **Financial Machine Learning**, with proven applications in:  

- **Intelligent trading agents for HFT dashboards**  
- Customer churn prediction  
- Credit risk modeling  
- Time-series forecasting  
- Advanced data analysis and decision support  


### Systems & Infrastructure  

Specialized in high-performance architectures and real-time data processing pipelines, ensuring low-latency execution, scalability, and production reliability.

### Tools & Frameworks  

Extensive hands-on experience with **TensorFlow**, **PyTorch**, **Scikit-learn**, and **Pandas** for AI development.  

Proficient with **Docker**, **Kubernetes**, **Jenkins**, **AWS**, and **Azure** for **cloud-native deployment** and **orchestration**.  

### Professional Strengths  

- Strong **problem-solving** and analytical mindset  
- Ability to **translate business requirements into technical solutions**  
- Solid background in **quantitative analysis** and **project management**  
- Clear and effective **communication** in cross-functional teams  

---

## 🚀 Current Project Highlight  

- **High-Frequency Trading Dashboard with Intelligent Agents**  
  Developing a next-generation **real-time trading dashboard** that integrates:  
  - **C++/Python low-latency pipelines**  
  - **Agent-based architecture** for market prediction, communication, and execution  
  - **AI/ML modules** (LLMs, deep learning, financial ML) for adaptive strategies  
  - **Scalable backend** with **Docker, Kubernetes, and ClickHouse** for real-time data storage and analytics  

This project bridges **cutting-edge AI** with **HFT infrastructure**, aiming to deliver both **speed** and **intelligence** in financial decision-making.  

---

## Online Tutoring Booking Dashboard (in development)

Building an online booking dashboard for a tutoring service with focus on reliability, usability and scalability. Core features and stack:

- Tech stack: Laravel (PHP 8.x), MySQL/PostgreSQL, Redis (caching/queues), Vue.js (or React) for the frontend, Tailwind CSS, Docker, Nginx, Let's Encrypt, Stripe for payments.
- Key features:
  - Real-time availability calendar and multi-timezone scheduling
  - Booking management for tutors and students, rescheduling and cancellations
  - Secure user authentication, role-based access (admins, tutors, students)
  - Online payments, invoices and refund handling via Stripe
  - Email/SMS/push notifications and reminders (Celery-like queues via Redis)
  - Admin dashboard with analytics: bookings, revenue, tutor utilization
  - Lesson materials, session notes and attachments
  - Tests, CI/CD pipelines, containerized deployments and monitoring (Prometheus/Grafana)
- Goals: provide a polished UX for students, an efficient management interface for tutors, and a robust, production-ready backend able to scale with demand.
 
---

## How I update this page (commands)

Below are the exact commands I run locally to regenerate artifacts, build the site and deploy the generated `_site` folder without tracking generated files in Git. Use the variant that fits your environment (Bundler, user gems, or Docker).

1. Regenerate CV JSON (if your workflow includes it):

```bash
python3 scripts/cv_yaml_to_json.py
```

1. Ensure Ruby Gems path (if you installed gems in your home directory):

```bash
export PATH="$HOME/.local/share/gem/ruby/3.4.0/bin:$PATH"
```

1. Clean and build the site:

```bash
jekyll clean
jekyll build --trace
```

If you use Bundler (recommended for reproducible builds):

```bash
bundle config set --local path 'vendor/bundle'
bundle install --jobs 4 --retry 3
JEKYLL_ENV=production bundle exec jekyll build --trace
```

1. Serve locally for a quick preview with live reload:

```bash
bundle exec jekyll serve --livereload
# or
jekyll serve --livereload
```

1. Deploy the generated `_site` to your server (example using rsync):

```bash
rsync -avz --delete _site/ user@server:/path/to/website
# or with scp
scp -r _site/* user@server:/path/to/website
```

1. Commit only source changes (do not commit `_site`):

```bash
git add index.md _data/cv.yml
git commit -m "chore(site): update homepage and docs"
git push origin main
```

Notes:

- `DEPLOYMENT.md` contains the same instructions and is added to `.gitignore` so it won't be tracked by Git.

- If you prefer Docker, you can build/serve with the official Jekyll image:

```bash
docker run --rm -v "$PWD":/srv/jekyll -it jekyll/jekyll:4 jekyll build --trace
docker run --rm -v "$PWD":/srv/jekyll -p 4000:4000 -it jekyll/jekyll:4 jekyll serve --livereload
```


