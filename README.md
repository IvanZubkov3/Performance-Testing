# 🚀 Performance Testing with Taurus, JMeter & Allure

This project automates **API performance testing** using **Taurus and JMeter** with **detailed Allure reports**.

## 📌 Features
✔️ **Runs API performance tests** on `https://reqres.in`.  
✔️ **Supports HTTP Methods**: `GET`, `POST`, `PUT`, `HEAD`, `DELETE`.  
✔️ **Generates Allure Reports** for tracking performance history.  
✔️ **Supports CI/CD automation with GitHub Actions**.  (In Progress)

---

## 📌 Tools Used
| Tool       | Purpose |
|------------|---------|
| **Python 3.11+** | Required for running Taurus & Allure |
| **Taurus (`bzt`)** | Simplifies JMeter performance tests |
| **JMeter 5.5** | Performance testing tool for APIs |
| **Allure Reports** | Test report visualization |
| **GitHub Actions** | Automates test execution |
| **VS Code** | Recommended IDE |

---

Run Taurus tests:
bzt test.yml

---
Generating & Viewing Allure Reports:
allure serve reports/allure-results
