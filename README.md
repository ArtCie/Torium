# Torium
## General project description can be found here:

[TORIUM-Torium-generalinfo-280123-0718.pdf](https://github.com/ArtCie/Torium-BE/files/10526560/TORIUM-Torium-generalinfo-280123-0718.pdf)

## Requirements
```
boto3==1.26.14
botocore==1.29.14
Flask==2.2.2
flask_cors==3.0.10
psycopg2==2.9.5
```

## **Architecture**

Whole architecture integrates 13 AWS Services:

**IAM** - resources permissions

**SQS** - communication between API and Lambda functions

**Lambda** - micro services

**Relational Database Service** - Relational PostgreSQL Database

**S3** - object storage

**Secrets Manager** - store and fetch DB credentials

**Cognito** - user authentication module

**Amplify** - integration with Flutter app

**CloudWatch** - logs

**SNS** - handling PUSH notifications and SMS messages

**SES** - send email

**EventBridge** - launch resources periodically


<br />

---

<br />

### **Lambda functions**

### **Cognito handlers**

#### **cognito-preSignUp**

Trigger - cognito user pool

General Use Case - save user to database after registration

Input - user email + cognito user id

Output - None

<br />

**Data Flow**

<img width="961" alt="Screenshot 2023-01-28 at 11 00 36" src="https://user-images.githubusercontent.com/72509444/215260197-3dcfc3c4-cf00-4a3f-b54f-9bc435873067.png">

<br />

#### **cognito-postSignUp**

Trigger - cognito user pool

General Use Case - after succesfull registration update user status to confirmed

Input - cognito user id

Output - None

<br />

**Data Flow**

<img width="826" alt="Screenshot 2023-01-28 at 11 01 21" src="https://user-images.githubusercontent.com/72509444/215260229-0b79cb8b-b244-4a53-8afc-1a2aff217384.png">

<br />

### **Schedule and send notifications**

#### **schedule-events**

Trigger - AWS EventBridge schedule

General Use Case - select all events for which notification should be triggered

Input - None

Output - send SQS message to schedule-notifications-queue.fifo for each event to be triggered - event_id + event_timestamp


<br />

#### **schedule-notifications**

Trigger - SQS schedule-notifications-queue.fifo queue

General Use Case - insert log + select users to send reminders - forward to service that send notification

Input - event_id + event_timestamp

Output - send SQS message to send-sms.fifo, send-email.fifo or send-pushNotification-queue.fifo for each notification to be sent - message + user_id + event_reminders_id + event_timestamp + information about receiver (phone_number, email or device_arn)


<br />

#### **send-sms**

Trigger - SQS send-sms.fifo queue

General Use Case - send SMS with reminder and save information to logs

Input - user_id + timestamp + event_reminders_id + mobile_number + message

Output - None


<br />

#### **send-email**

Trigger - SQS send-email.fifo queue

General Use Case - send email with reminder and save information to logs

Input - user_id + timestamp + event_reminders_id + email_address + message

Output - None


<br />

#### **send-pushNotification**

Trigger - SQS send-pushNotification-queue.fifo queue

General Use Case - send PUSH with reminder and save information to logs

Input - user_id + timestamp + event_reminders_id + device_arn + message

Output - None


<br />

**Data Flow**

<img width="1267" alt="Screenshot 2023-01-28 at 11 03 47" src="https://user-images.githubusercontent.com/72509444/215260332-7dd6f3b0-83b6-468b-abce-8196e91e94a1.png">

<br />

### **Send additional PUSH notifications**

#### **send-pushGroupInvitation**

Trigger - SQS send_push_group_invitation-queue.fifo queue

General Use Case - send PUSH with group invitation to user

Input - user_id + group_invitation_logs_id + group_id + timestamp

Output - None


<br />

**Data Flow**

<img width="1001" alt="Screenshot 2023-01-28 at 11 06 39" src="https://user-images.githubusercontent.com/72509444/215260502-2e307f49-4dbf-44a5-89d4-76e898089429.png">

<br />

#### **schedule-pushNotification-comments**

Trigger - SQS schedule-push-notification-comments-queue.fifo queue

General Use Case - send PUSH about new comment to each event member

Input - user_id + timestamp + events_comments_id + event_id + comment

Output - None

<br />

**Data Flow**

<img width="1003" alt="Screenshot 2023-01-28 at 11 05 42" src="https://user-images.githubusercontent.com/72509444/215260476-847c1c8d-16cc-44b3-8972-a74999440541.png">

<br />

### **DevOps**

#### **torium-alerts**

Trigger - EventBridge event execute periodically

General Use Case - go through all AWS resources, find bugs and send errors to Discord

Input - None

Output - Discord Notifications

<br />

**Data Flow**

<img width="672" alt="Screenshot 2023-01-28 at 11 07 19" src="https://user-images.githubusercontent.com/72509444/215260578-f6176e60-f36f-4fb0-9b22-d55128dfbd71.png">


<br />

---

<br />

## Elastic Beanstalk API

28 endpoints implemented in Python using Flask framework - server is set up in EC2 using Elastic Beanstalk service.
Completed schema can be found in EB/torium-api/api-schema.json

<img width="1383" alt="Screenshot 2023-01-28 at 11 17 43" src="https://user-images.githubusercontent.com/72509444/215261247-5308685d-ba76-4178-8f83-c9de77292ce2.png">


### Event endpoints

#### /event
methods - POST, GET, PUT, DELETE

#### /event/notify
methods - POST

#### /event/comment
methods - POST, GET, PUT, DELETE

### Group endpoints

#### /groups
methods - POST, GET, PUT, DELETE

#### /groups/invitation
methods - GET

#### /groups/invitation/count
methods - GET

#### /group/members
methods - GET, DELETE, POST

#### /group/members/status
methods - PATCH

#### /group/members/role
methods - PATCH

### Organization endpoints

#### /organizations
methods - GET

### Users endpoints

#### /users
methods - GET

#### /users/preferences
methods - PATCH

#### /users/mobile
methods - POST, PATCH

#### /users/organization
methods - PATCH

#### /users/device
methods - PATCH

#### /users/email
methods - GET

---

Feel free to contact me if you have any questions, more than happy to answer :) 
