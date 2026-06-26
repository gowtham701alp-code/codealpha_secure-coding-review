# Secure Coding Review

## Overview

This project demonstrates a basic Python login application containing intentional security vulnerabilities for educational purposes. The objective is to identify these vulnerabilities, assess their risks, and recommend secure coding practices.

---

## Objective

* Perform a secure coding review.
* Identify common security vulnerabilities.
* Understand their impact.
* Recommend secure coding techniques.

---

## Technologies Used

* Python
* SQLite

---

## Project Files

* **vulnerable_login.py** – Vulnerable login application.
* **Secure_Coding_Review_Report.pdf** – Security review report.
* **README.md** – Project documentation.

---

# Vulnerability Analysis

## 1. SQL Injection

**Description**

The SQL query is created by directly concatenating user input into the SQL statement.

**Risk Level**

High

**Impact**

An attacker can bypass authentication or access unauthorized data.

**Recommended Fix**

Use parameterized SQL queries.

---

## 2. Hardcoded Database Connection

**Description**

The database connection is hardcoded inside the source code.

**Risk Level**

Medium

**Impact**

Configuration changes require modifying the source code.

**Recommended Fix**

Store configuration values in environment variables or configuration files.

---

## 3. Lack of Input Validation

**Description**

The application accepts any user input without validation.

**Risk Level**

Medium

**Impact**

Unexpected input may cause application errors or assist attackers.

**Recommended Fix**

Validate and sanitize all user inputs.

---

## 4. Poor Error Handling

**Description**

Database exceptions are displayed directly to the user.

**Risk Level**

Low

**Impact**

Attackers may gain information about the application's internal structure.

**Recommended Fix**

Display generic error messages and log detailed errors securely.

---

## Learning Outcomes

Through this project, I learned about:

* SQL Injection attacks
* Secure authentication
* Input validation
* Error handling
* Secure coding principles

---

## Conclusion

Secure coding practices help protect applications from common cyberattacks. Identifying and fixing vulnerabilities such as SQL Injection, improper input validation, and insecure error handling significantly improves application security.
