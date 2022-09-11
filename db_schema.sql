CREATE TYPE reminder_preferences_type AS ENUM ('SMS', 'PUSH', 'EMAIL');
CREATE TYPE status_type AS ENUM('confirmed', 'pending', 'rejected');
CREATE TYPE reminder_type AS ENUM('periodical', 'once');
CREATE TYPE event_reminders_logs_status_type AS ENUM('delivered', 'failed', 'answered');


CREATE TABLE users(
    id serial4 NOT NULL,
    username varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    mobile_number varchar(50) NOT NULL,
    "timestamp" timestamp NOT NULL,
	is_confirmed bool NOT NULL,
	reminder_preferences reminder_preferences_type NULL,
    CONSTRAINT users_PK PRIMARY KEY (id)
);

CREATE TABLE "groups"(
	id serial4 NOT NULL,
	name varchar(50) NOT NULL,
	admin_id int4 NOT NULL,
	"timestamp" timestamp NOT NULL,
	CONSTRAINT groups_PK PRIMARY KEY(id)
);

ALTER TABLE "groups" ADD CONSTRAINT groups_aID_FK FOREIGN KEY (admin_id) REFERENCES users(id);

CREATE TABLE users_groups(
	id serial4 NOT NULL,
	group_id int4 NOT NULL,
	user_id int4 NOT NULL,
	"timestamp" timestamp NOT NULL,
	CONSTRAINT users_groups_PK PRIMARY KEY(id)
);
ALTER TABLE users_groups ADD CONSTRAINT user_groups_gID_FK FOREIGN KEY(group_id) REFERENCES "groups"(id);
ALTER TABLE users_groups ADD CONSTRAINT user_groups_uID_FK FOREIGN KEY(user_id) REFERENCES users(id);


CREATE TABLE group_invitation_logs(
	id serial4 NOT NULL,
	group_id int4 NOT NULL,
	user_to int4 NOT NULL,
	"timestamp" timestamp NOT NULL,
	status status_type NOT NULL,
	updated_timestamp timestamp NULL,
	CONSTRAINT group_invitation_logs_PK PRIMARY KEY(id)
);
ALTER TABLE group_invitation_logs ADD CONSTRAINT user_groups_utID_FK FOREIGN KEY(user_to) REFERENCES users(id);
ALTER TABLE group_invitation_logs ADD CONSTRAINT user_groups_gID_FK FOREIGN KEY(group_id) REFERENCES "groups"(id);

CREATE TABLE events(
	id serial4 NOT NULL,
	is_budget bool NOT NULL,
	budget float4 NULL,
	description varchar(500) NULL,
	group_id int4 NOT NULL,
	"timestamp" timestamp NOT NULL,
	updated_timestamp timestamp NULL,
	reminder reminder_type NOT NULL,
	schedule_period interval NOT NULL,
	CONSTRAINT events_PK PRIMARY KEY(id)
);
ALTER TABLE events ADD CONSTRAINT events_gID_FK FOREIGN KEY(group_id) REFERENCES "groups"(id);

CREATE TABLE event_reminders(
	id serial4 NOT NULL,
	event_id int4 NOT NULL,
	trigger_timestamp timestamp NOT NULL,
	"timestamp" timestamp NOT NULL,
	CONSTRAINT events_reminders_PK PRIMARY KEY(id)
);
ALTER TABLE event_reminders ADD CONSTRAINT event_reminders_eID_FK FOREIGN KEY(event_id) REFERENCES events(id);


CREATE TABLE event_reminders_logs(
	id serial4 NOT NULL,
	event_reminders_id int4 NOT NULL,
	sent_timestamp timestamp NOT NULL,
	user_id int4 NOT NULL,
	status event_reminders_logs_status_type NOT NULL,
	answer varchar(10) NULL,
	"timestamp" timestamp NOT NULL,
	CONSTRAINT event_reminders_logs_PK PRIMARY KEY(id)
);
ALTER TABLE event_reminders_logs ADD CONSTRAINT event_reminders_logs_erID_FK FOREIGN KEY(event_reminders_id) REFERENCES event_reminders(id);
ALTER TABLE event_reminders_logs ADD CONSTRAINT event_reminders_logs_uID_FK FOREIGN KEY(user_id) REFERENCES users(id);
