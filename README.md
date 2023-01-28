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

## Architecture

### Lambda functions

### Cognito handlers

#### cognito-preSignUp

Trigger - cognito user pool

General Use Case - save user to database after registration

Input - user email + cognito user id

Output - None


#### cognito-postSignUp

Trigger - cognito user pool

General Use Case - after succesfull registration update user status to confirmed

Input - cognito user id

Output - None


### Schedule and send notifications



#### schedule-events

Trigger - AWS EventBridge schedule

General Use Case - select all events for which notification should be triggered

Input - None

Output - send SQS message to schedule-notifications-queue.fifo for each event to be triggered - event_id + event_timestamp



#### schedule-notifications

Trigger - SQS schedule-notifications-queue.fifo queue

General Use Case - insert log + select users to send reminders - forward to service that send notification

Input - event_id + event_timestamp

Output - send SQS message to send-sms.fifo, send-email.fifo or send-pushNotification-queue.fifo for each notification to be sent - message + user_id + event_reminders_id + event_timestamp + information about receiver (phone_number, email or device_arn)



#### send-sms

Trigger - SQS send-sms.fifo queue

General Use Case - send SMS with reminder and save information to logs

Input - user_id + timestamp + event_reminders_id + mobile_number + message

Output - None



#### send-email

Trigger - SQS send-email.fifo queue

General Use Case - send email with reminder and save information to logs

Input - user_id + timestamp + event_reminders_id + email_address + message

Output - None



#### send-pushNotification

Trigger - SQS send-pushNotification-queue.fifo queue

General Use Case - send PUSH with reminder and save information to logs

Input - user_id + timestamp + event_reminders_id + device_arn + message

Output - None



### Send additional PUSH notifications



#### send-pushGroupInvitation

Trigger - SQS send_push_group_invitation-queue.fifo queue

General Use Case - send PUSH with group invitation to user

Input - user_id + group_invitation_logs_id + group_id + timestamp

Output - None



#### schedule-pushNotification-comments

Trigger - SQS schedule-push-notification-comments-queue.fifo queue

General Use Case - send PUSH about new comment to each event member

Input - user_id + timestamp + events_comments_id + event_id + comment

Output - None

#### torium-alerts

Trigger - EventBridge event execute periodically

General Use Case - go through all AWS resources, find bugs and send errors to Discord

Input - None

Output - Discord Notifications

