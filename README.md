# aws-serverless-url-shortener

A production-ready serverless URL shortener built on AWS.
Fully provisioned with Terraform. No servers to manage.

## Architecture

> Architecture diagram coming soon — building now

### How it works
1. User submits a long URL via the web frontend
2. Frontend calls API Gateway endpoint (HTTPS)
3. Lambda function (Python) generates a short code
4. Short code + original URL saved to DynamoDB
5. User receives short URL — redirects handled by Lambda

### AWS Services used
- S3 + CloudFront — static frontend hosting
- API Gateway — REST API (HTTPS)
- Lambda (Python 3.11) — business logic
- DynamoDB — URL storage (on-demand)
- IAM — least-privilege roles
- CloudWatch — monitoring and alerts
- Terraform — all infrastructure as code

## Project Status
- [x] Repository created and structured
- [ ] Lambda function written
- [ ] Terraform infrastructure code
- [ ] Frontend deployed to S3
- [ ] CloudWatch monitoring added
- [ ] Demo video recorded

## What I am learning
- Designing stateless serverless functions
- DynamoDB key design patterns
- Terraform state management
- CloudFront CDN configuration

## How to deploy (coming soon)
Instructions will be added once build is complete.

## Author
Vishwajeet Suryawanshi — Aspiring Cloud Engineer
GitHub: https://github.com/vishwajeet-aws
