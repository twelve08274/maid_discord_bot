# 42 API Documentation

> Base URL: `https://api.intra.42.fr/v2`
> Authentication: OAuth2
> Format: JSON

## リソース一覧

- [accreditations](#accreditations) — Accreditations
- [achievements](#achievements) — Meta-goals earned by [users](#users) all along their progression.
- [achievements_users](#achievements_users) — [Users](#users) which earned an [achievement](#achievement)
- [alumnized_users](#alumnized_users) — Alumnized users
- [amendments](#amendments) — Modifications applied to an [internship](#internship).
- [announcements](#announcements) — An announcement made to [users](#users) in a [cursus](#cursus) on their homepage.
- [anti_grav_units](#anti_grav_units)
- [anti_grav_units_users](#anti_grav_units_users)
- [apps](#apps) — Applications for the API v2
- [attachments](#attachments) — All data which can be linked, like [videos](#videos), [pdfs](#pdfs), or [links](#links).
- [balances](#balances) — The [balance](#balances) of a [pool](#pools)
- [bloc_deadlines](#bloc_deadlines) — A [bloc](#bloc_deadlines>Bloc Deadlines is the beginning and the end of a yearly tournament for a <a href=)
- [blocs](#blocs) — A [bloc](#blocs) is the managing container of [coalitions](#coalitions).
- [broadcasts](#broadcasts) — Broadcasts publicated on a campus
- [campus](#campus) — Places where 42 [users](#users) works
- [campus_users](#campus_users) — The [users](#users) wich are in a [campus](#campus)
- [certificates](#certificates) — [certificates](#certificates)
- [certificates_users](#certificates_users) — [User](#users) belonging to a [certificate](#certificates).
- [closes](#closes) — The closing of a 42 account
- [clusters](#clusters) — The clusters
- [coalitions](#coalitions) — A [users](#coalitions>coalition is group of <a href=) competing inside of a [bloc](#blocs).
- [coalitions_users](#coalitions_users) — [coalition](#users>Users belonging to a <a href=).
- [commands](#commands) — Products are sold on the intranet shop, here are commands
- [community_services](#community_services) — A task that an [user](#users) have to do for the community. Usually linked with a [close](#closes).
- [companies](#companies) — Companies from companies website
- [correction_point_historics](#correction_point_historics)
- [cursus](#cursus) — An educational cycle in 42
- [cursus_users](#cursus_users) — The [users](#users) wich are in a [cursus](#cursus)
- [dashes](#dashes) — The [Dash](#dashs) is a short-time [project](#projects)
- [dashes_users](#dashes_users) — The [dash](#dashes) of a [user](#users)
- [endpoints](#endpoints) — A endpoint for a [campus](#campus)
- [evaluations](#evaluations) — The [Evaluation](#dashs) of a [project](#projects)
- [events](#events) — The events in a [campus](#campus) or a [cursus](#cursus)
- [events_users](#events_users) — [Users](#users) registered to an [event](#events)
- [exams](#exams) — The exam in a [campus](#campus) or a [cursus](#cursus)
- [exams_users](#exams_users)
- [experiences](#experiences) — An experience gained by an [user](#users) in a particular [skill](#skills).
- [expertises](#expertises) — Pedagogic expertises
- [expertises_users](#expertises_users) — [Users](#users) which have an [expertise](#expertises)
- [feedbacks](#feedbacks) — The feedback of a [ScaleTeam](#scale_teams) or an [Event](#events)
- [flags](#flags) — Flags from scales
- [flash_users](#flash_users) — The [Flash Users](#flash_users)
- [flashes](#flashes) — The [Flash](#flashes)
- [gitlab_users](#gitlab_users)
- [groups](#groups) — Groups in which [users](#users) belong to. It will display a label on their profile and on the forum.
- [groups_users](#groups_users) — [Users](#users) who are in a [group](#group).
- [internships](#internships) — The [internship](#internships)
- [journals](#journals)
- [languages](#languages) — The [language](#languages)
- [languages_users](#languages_users) — The [languages](#languages) of a [user](#users)
- [levels](#levels) — A level indicator for a [cursus](#cursus).
- [locations](#locations) — The location of an user in a [campus](#campus)
- [mailings](#mailings) — Mails from and between 42 entities
- [notes](#notes) — A note for an [user](#users)
- [notions](#notions) — The elearning notion in a [cursus](#cursus)
- [offers](#offers) — Offers from companies website
- [offers_users](#offers_users) — [Users](#users) who have subscribed to an [offer](#title).
- [params_project_sessions_rules](#params_project_sessions_rules) — The value of a parameter for a [project sessions rule](#project_sessions_rules).
- [partnerships](#partnerships) — Pedagogic partnerships
- [partnerships_users](#partnerships_users) — [Users](#users) doing a [partnership](#partnerships)
- [patronages](#patronages) — A patronage between two [users](#users)
- [patronages_reports](#patronages_reports) — A [report](#reports) for a [patronage](#patronages)
- [pools](#pools) — The [pool](#pools) of evaluation points.
- [products](#products) — Products are sold on the intranet shop
- [project_data](#project_data) — [Project](#projects) data for the graph
- [project_sessions](#project_sessions) — A project session defines a particular behaviour for a [project](#projects), based on the [cursus](#cursus) and / or the [campus](#campus) .
- [project_sessions_rules](#project_sessions_rules) — A [rule](#rules) linked to a project session.
- [project_sessions_skills](#project_sessions_skills) — A [skill](#skills) linked to a project session.
- [projects](#projects) — Pedagogic projects of a [cursus](#cursus)
- [projects_users](#projects_users) — [Users](#users) which did or are doing a [project](#projects)
- [quests](#quests) — Quests which can or must be done by [users](#users)
- [quests_users](#quests_users) — [Users](#users) which earned an [quest](#quest)
- [roles](#roles) — Grants particular privileges to entities like [users](#users) and [applications](#apps)
- [roles_entities](#roles_entities) — The [applications](#apps) linked to a role
- [rules](#rules) — A rule for a [project](#projects)
- [scale_teams](#scale_teams) — A defence of a [team](#teams) (on a [project](#projects)), involving an evaluator
- [scales](#scales) — A scale is composed by questions which allows an [users](#users) to rate the quality of a [project](#projects) .
- [scores](#scores) — Points given to a [coalition](#coalitions).
- [skills](#skills) — A particlar skill.
- [slots](#slots) — The slots available to [users](#users) for booking a [project](#projects) [scale team](#scale_teams).
- [squads](#squads) — A [squads](#squads) is the managing container of [squads_users](#squads_users).
- [squads_users](#squads_users) — A [squads_users](#squads_users) will group users inside a same coalition
- [subnotions](#subnotions) — The elearning subnotion in a [notion](#notions)
- [tags](#tags) — Non-hierarchical keyword, acting as a meta-data and helping to describe entities.
- [tags_users](#tags_users) — Resource associating a [User](#users) and a [Tag](#tags).
- [teams](#teams) — One or many [users](#users) which have to finish a [project](#projects) together.
- [teams_uploads](#teams_uploads) — An uploaded mark for a [team](#teams), given by a bot (like the Moulinette), without any defence.
- [teams_users](#teams_users) — [Team](#teams) composed of one [User](#users)
- [titles](#titles) — Titles a [user](#users) can obtain, generally through achievements. It will be displayed on their profile and on the forum.
- [titles_users](#titles_users) — [Users](#users) who have a [title](#title).
- [transactions](#transactions) — Transaction represents Altarian Dollars earned.
- [translations](#translations) — Translations
- [user_candidatures](#user_candidatures) — The candidature of an [user](#users)
- [users](#users) — A 42 student, staff, or any entity with a 42 account.
- [waitlists](#waitlists) — Waitlist for an [event](#events) or an [exam](#exams).
- [webhook_registeries](#webhook_registeries) — Webhook Registeries

---

## attachments

All data which can be linked, like [videos](#videos), [pdfs](#pdfs), or [links](#links).

### attachments / index

**GET** `/v2/project_sessions/:project_session_id/attachments`

**GET** `/v2/projects/:project_id/attachments`

**GET** `/v2/attachments`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `project_id` | No | string | The project id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>attachable_id</code>, <code>attachable_type</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>language_id</code>, <code>user_id</code>, <code>default</code>, <code>up_to_date</code>, <code>container_id</code>, <code>container_type</code>, <code>base_id</code>, <code>untranslatable</code>, <code>attachments_structure_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>attachable_id</code>, <code>attachable_type</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>language_id</code>, <code>user_id</code>, <code>default</code>, <code>up_to_date</code>, <code>container_id</code>, <code>container_type</code>, <code>base_id</code>, <code>untranslatable</code>, <code>attachments_structure_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>attachable_id</code>, <code>attachable_type</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>language_id</code>, <code>user_id</code>, <code>default</code>, <code>up_to_date</code>, <code>container_id</code>, <code>container_type</code>, <code>base_id</code>, <code>untranslatable</code>, <code>attachments_structure_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### attachments / show

**GET** `/v2/project_sessions/:project_session_id/attachments/:id`

**GET** `/v2/attachments/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### attachments / create

**POST** `/v2/projects/:project_id/attachments`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_id` | Yes | string | The project id or slug (Must be String |
| `attachment` | No | hash | Must be a Hash |

### attachments / update

**PATCH** `/v2/attachments/:id`

**PUT** `/v2/attachments/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `attachment` | No | hash | Must be a Hash |

### attachments / destroy

**DELETE** `/v2/attachments/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## accreditations

Accreditations

### accreditations / index

**GET** `/v2/accreditations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>user_id</code>, <code>cursus_id</code>, <code>difficulty</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>user_id</code>, <code>cursus_id</code>, <code>difficulty</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>user_id</code>, <code>cursus_id</code>, <code>difficulty</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### accreditations / show

**GET** `/v2/accreditations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### accreditations / create

**POST** `/v2/accreditations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `accreditation` | No | hash | Must be a Hash |

### accreditations / update

**PATCH** `/v2/accreditations/:id`

**PUT** `/v2/accreditations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `accreditation` | No | hash | Must be a Hash |

### accreditations / destroy

**DELETE** `/v2/accreditations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## achievements

Meta-goals earned by [users](#users) all along their progression.

### achievements / index

**GET** `/v2/achievements`

**GET** `/v2/cursus/:cursus_id/achievements`

**GET** `/v2/campus/:campus_id/achievements`

**GET** `/v2/titles/:title_id/achievements`

List all visibles achievements. Invisibles achievements need at least the `basic_staff` role.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `title_id` | No | string | The title id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>internal_name</code>, <code>kind</code>, <code>tier</code>, <code>description</code>, <code>pedago</code>, <code>visible</code>, <code>nbr_of_success</code>, <code>parent_id</code>, <code>image</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>position</code>, <code>reward</code>, <code>title_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>internal_name</code>, <code>kind</code>, <code>tier</code>, <code>description</code>, <code>pedago</code>, <code>visible</code>, <code>nbr_of_success</code>, <code>parent_id</code>, <code>image</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>position</code>, <code>reward</code>, <code>title_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>internal_name</code>, <code>kind</code>, <code>tier</code>, <code>description</code>, <code>pedago</code>, <code>visible</code>, <code>nbr_of_success</code>, <code>parent_id</code>, <code>image</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>position</code>, <code>reward</code>, <code>title_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### achievements / show

**GET** `/v2/achievements/:id`

Return the achievement specified by the `:id` parameter. Invisibles achievements need at least the `basic_staff` role.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### achievements / create

**POST** `/v2/achievements`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `achievement` | No | hash | Must be a Hash |

### achievements / update

**PATCH** `/v2/achievements/:id`

**PUT** `/v2/achievements/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `achievement` | No | hash | Must be a Hash |

### achievements / destroy

**DELETE** `/v2/achievements/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## achievements_users

[Users](#users) which earned an [achievement](#achievement)

### achievements_users / index

**GET** `/v2/achievements/:achievement_id/achievements_users`

**GET** `/v2/achievements_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `achievement_id` | No | string | The achievement id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>achievement_id</code>, <code>nbr_of_success</code>, <code>created_at</code>, <code>updated_at</code>, <code>rewarded</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>achievement_id</code>, <code>nbr_of_success</code>, <code>created_at</code>, <code>updated_at</code>, <code>rewarded</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>achievement_id</code>, <code>nbr_of_success</code>, <code>created_at</code>, <code>updated_at</code>, <code>rewarded</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### achievements_users / show

**GET** `/v2/achievements_users/:id`

Return the achievement specified by the `:id` parameter

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### achievements_users / create

**POST** `/v2/achievements_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `achievements_user` | No | hash | Must be a Hash |

### achievements_users / update

**PATCH** `/v2/achievements_users/:id`

**PUT** `/v2/achievements_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `achievements_user` | No | hash | Must be a Hash |

### achievements_users / destroy

**DELETE** `/v2/achievements_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## alumnized_users

Alumnized users

### alumnized_users / index

**GET** `/v2/alumnized_users` — Get all alumnized users for a given campus

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `alumnized_since` | No | string | The date since the user was alumnized (Must be DateTime |
| `campus_id` | Yes | numeric | The campus ID (Must be Integer |

## amendments

Modifications applied to an [internship](#internship).

### amendments / index

**GET** `/v2/amendments`

**GET** `/v2/users/:user_id/amendments`

**GET** `/v2/internships/:internship_id/amendments`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `internship_id` | No | string | The internship id (Must be String |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |
| `amendment` | No | hash | Must be a Hash |

### amendments / show

**GET** `/v2/amendments/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `amendment` | No | hash | Must be a Hash |

### amendments / create

**POST** `/v2/amendments`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `amendment` | No | hash | Must be a Hash |

### amendments / destroy

**DELETE** `/v2/amendments/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `amendment` | No | hash | Must be a Hash |

## announcements

An announcement made to [users](#users) in a [cursus](#cursus) on their homepage.

### announcements / graph

**GET** `/v2/announcements/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>expire_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by expire_at desc, id desc by default. (Must be one of: <code>id</code>, <code>author</code>, <code>title</code>, <code>text</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>image</code>, <code>expire_at</code>, <code>link</code>, <code>notificable_id</code>, <code>notificable_type</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>author</code>, <code>title</code>, <code>text</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>image</code>, <code>expire_at</code>, <code>link</code>, <code>notificable_id</code>, <code>notificable_type</code>, <code>expire</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>author</code>, <code>title</code>, <code>text</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>image</code>, <code>expire_at</code>, <code>link</code>, <code>notificable_id</code>, <code>notificable_type</code>. |

### announcements / filtering_keys

Return all the announcements, globally or # filtered by cursus

### announcements / show

**GET** `/v2/announcements/:id`

Return the announcement specified by the `:id` parameter

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### announcements / create

**POST** `/v2/announcements`

**POST** `/v2/cursus/:cursus_id/announcements`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `announcement` | No | hash | Must be a Hash |

### announcements / update

**PATCH** `/v2/announcements/:id`

**PUT** `/v2/announcements/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `announcement` | No | hash | Must be a Hash |

### announcements / destroy

**DELETE** `/v2/announcements/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## anti_grav_units

### anti_grav_units / index

**GET** `/v2/anti_grav_units`

### anti_grav_units / show

**GET** `/v2/anti_grav_units/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## anti_grav_units_users

### anti_grav_units_users / index

**GET** `/v2/anti_grav_units_users`

**GET** `/v2/users/:user_id/anti_grav_units_users`

**GET** `/v2/campus/:campus_id/anti_grav_units_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>close_id</code>, <code>is_free</code>, <code>reason</code>, <code>end_date</code>, <code>expected_end_date</code>, <code>begin_date</code>, <code>anti_grav_unit_id</code>, <code>internship_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>close_id</code>, <code>is_free</code>, <code>reason</code>, <code>end_date</code>, <code>expected_end_date</code>, <code>begin_date</code>, <code>anti_grav_unit_id</code>, <code>internship_id</code>, <code>cursus_id</code>, <code>active</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>close_id</code>, <code>is_free</code>, <code>reason</code>, <code>end_date</code>, <code>expected_end_date</code>, <code>begin_date</code>, <code>anti_grav_unit_id</code>, <code>internship_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### anti_grav_units_users / show

**GET** `/v2/anti_grav_units_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### anti_grav_units_users / create

**POST** `/v2/anti_grav_units_users`

Create an AntiGravUnitsUser, if is_free is true then the AGU user will not loose an agu or freeze time.

This is the api for creating agu that ends in the future. If you are looking for creating agu in the past to delay the blackhole, please go to the following link. [POST /v2/users/:user_id/free_past_agu](/apidoc/2.0/users/free_past_agu.html)

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `anti_grav_units_user` | No | hash | Must be a Hash |

### anti_grav_units_users / update

**PATCH** `/v2/anti_grav_units_users/:id`

**PUT** `/v2/anti_grav_units_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `anti_grav_units_user` | No | hash | Must be a Hash |

## apps

Applications for the API v2

### apps / index

**GET** `/v2/apps` — Get all the public and owned applications

**GET** `/v2/users/:user_id/apps` — Get all the public and owned applications

Return all the **public** created applications working with the APIv2.

If there is a resource owner, also returns the resource owner applications, **public or not**.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>token</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>allowed_origins</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>uid</code>, <code>owner_id</code>, <code>website</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>uid</code>, <code>owner_id</code>, <code>website</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### apps / show

**GET** `/v2/apps/:id` — Get a public or owned application

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## balances

The [balance](#balances) of a [pool](#pools)

### balances / index

**GET** `/v2/balances`

**GET** `/v2/pools/:pool_id/balances`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `pool_id` | No | string | The pool id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>pool_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>pool_id</code>, <code>future</code>, <code>end</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |
| `balance` | No | hash | Must be a Hash |

### balances / show

**GET** `/v2/balances/:id`

**GET** `/v2/pools/:pool_id/balances/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `pool_id` | No | string | The pool id (Must be String |
| `balance` | No | hash | Must be a Hash |

### balances / update

**PATCH** `/v2/balances/:id`

**PUT** `/v2/balances/:id`

**PATCH** `/v2/pools/:pool_id/balances/:id`

**PUT** `/v2/pools/:pool_id/balances/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `pool_id` | No | string | The pool id (Must be String |
| `balance` | No | hash | Must be a Hash |

## bloc_deadlines

A [bloc](#bloc_deadlines>Bloc Deadlines is the beginning and the end of a yearly tournament for a <a href=)

### bloc_deadlines / index

**GET** `/v2/bloc_deadlines`

**GET** `/v2/blocs/:bloc_id/bloc_deadlines`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | No | string | The bloc id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>bloc_id</code>, <code>begin_at</code>, <code>end_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>coalition_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### bloc_deadlines / show

**GET** `/v2/bloc_deadlines/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### bloc_deadlines / create

**POST** `/v2/bloc_deadlines`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_deadline` | No | hash | Must be a Hash |

### bloc_deadlines / update

**PATCH** `/v2/bloc_deadlines/:id`

**PUT** `/v2/bloc_deadlines/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `bloc_deadline` | No | hash | Must be a Hash |

## blocs

A [bloc](#blocs) is the managing container of [coalitions](#coalitions).

### blocs / index

**GET** `/v2/blocs`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>campus_id</code>, <code>squad_size</code>, <code>created_at</code>, <code>updated_at</code>, <code>coalition_delay</code>, <code>repeat_deadline_delay</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>campus_id</code>, <code>squad_size</code>, <code>created_at</code>, <code>updated_at</code>, <code>coalition_delay</code>, <code>repeat_deadline_delay</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### blocs / show

**GET** `/v2/blocs/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## broadcasts

Broadcasts publicated on a campus

### broadcasts / index

**GET** `/v2/campus/:campus_id/broadcasts`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus_id` | Yes | string | The campus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>campus_id</code>, <code>tag_id</code>, <code>content</code>, <code>pinned_until</code>, <code>hidden_at</code>, <code>url</code>, <code>created_at</code>, <code>updated_at</code>, <code>content_html</code>, <code>position</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>campus_id</code>, <code>tag_id</code>, <code>content</code>, <code>pinned_until</code>, <code>hidden_at</code>, <code>url</code>, <code>created_at</code>, <code>updated_at</code>, <code>content_html</code>, <code>position</code>, <code>hidden</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

## campus

Places where 42 [users](#users) works

### campus / index

**GET** `/v2/campus`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>time_zone</code>, <code>language_id</code>, <code>slug</code>, <code>main_email</code>, <code>endpoint_id</code>, <code>vogsphere_id</code>, <code>content_email</code>, <code>time_of_community_service_started</code>, <code>companies_mail</code>, <code>address</code>, <code>zip</code>, <code>city</code>, <code>country</code>, <code>pro_needs_validation</code>, <code>logo</code>, <code>website</code>, <code>facebook</code>, <code>twitter</code>, <code>display_name</code>, <code>email_extension</code>, <code>help_url</code>, <code>active</code>, <code>open_to_job_offers</code>, <code>default_hidden_phone</code>, <code>tig_email</code>, <code>minimum_slot_duration</code>, <code>alumni_system</code>, <code>manual_alumnization_before_first_internship</code>, <code>public</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>time_zone</code>, <code>language_id</code>, <code>slug</code>, <code>main_email</code>, <code>endpoint_id</code>, <code>vogsphere_id</code>, <code>content_email</code>, <code>time_of_community_service_started</code>, <code>companies_mail</code>, <code>address</code>, <code>zip</code>, <code>city</code>, <code>country</code>, <code>pro_needs_validation</code>, <code>logo</code>, <code>website</code>, <code>facebook</code>, <code>twitter</code>, <code>display_name</code>, <code>email_extension</code>, <code>help_url</code>, <code>active</code>, <code>open_to_job_offers</code>, <code>default_hidden_phone</code>, <code>tig_email</code>, <code>minimum_slot_duration</code>, <code>alumni_system</code>, <code>manual_alumnization_before_first_internship</code>, <code>public</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>time_zone</code>, <code>language_id</code>, <code>slug</code>, <code>main_email</code>, <code>endpoint_id</code>, <code>vogsphere_id</code>, <code>content_email</code>, <code>time_of_community_service_started</code>, <code>companies_mail</code>, <code>address</code>, <code>zip</code>, <code>city</code>, <code>country</code>, <code>pro_needs_validation</code>, <code>logo</code>, <code>website</code>, <code>facebook</code>, <code>twitter</code>, <code>display_name</code>, <code>email_extension</code>, <code>help_url</code>, <code>active</code>, <code>open_to_job_offers</code>, <code>default_hidden_phone</code>, <code>tig_email</code>, <code>minimum_slot_duration</code>, <code>alumni_system</code>, <code>manual_alumnization_before_first_internship</code>, <code>public</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### campus / show

**GET** `/v2/campus/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### campus / create

**POST** `/v2/campus`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus` | No | hash | Must be a Hash |

### campus / update

**PATCH** `/v2/campus/:id`

**PUT** `/v2/campus/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `campus` | No | hash | Must be a Hash |

### campus / stats

**GET** `/v2/campus/:campus_id/stats`

This endpoint is only for `42Network` app.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus` | No | hash | Must be a Hash |

## campus_users

The [users](#users) wich are in a [campus](#campus)

### campus_users / index

**GET** `/v2/campus_users`

**GET** `/v2/users/:user_id/campus_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>campus_id</code>, <code>is_primary</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>campus_id</code>, <code>is_primary</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>campus_id</code>, <code>is_primary</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### campus_users / show

**GET** `/v2/campus_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### campus_users / create

**POST** `/v2/campus_users`

**POST** `/v2/users/:user_id/campus_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `campus_user` | No | hash | Must be a Hash |

### campus_users / set_as_primary

**POST** `/v2/campus_users/:id/set_as_primary`

## certificates

[certificates](#certificates)

### certificates / index

**GET** `/v2/certificates`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |
| `certificate` | No | hash | Must be a Hash |

### certificates / show

**GET** `/v2/certificates/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `certificate` | No | hash | Must be a Hash |

## certificates_users

[User](#users) belonging to a [certificate](#certificates).

### certificates_users / index

**GET** `/v2/certificates_users`

**GET** `/v2/certificates/:certificate_id/certificates_users`

**GET** `/v2/users/:user_id/certificates_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `certificate_id` | No | string | The certificate id (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |
| `certificates_user` | No | hash | Must be a Hash |

### certificates_users / show

**GET** `/v2/certificates_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `certificates_user` | No | hash | Must be a Hash |

### certificates_users / destroy

**DELETE** `/v2/certificates_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `certificates_user` | No | hash | Must be a Hash |

## closes

The closing of a 42 account

### closes / index

**GET** `/v2/closes`

**GET** `/v2/users/:user_id/closes`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>closer_id</code>, <code>reason</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>end_at</code>, <code>jid</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>closer_id</code>, <code>reason</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>end_at</code>, <code>jid</code>, <code>campus_id</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>closer_id</code>, <code>reason</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>end_at</code>, <code>jid</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### closes / show

**GET** `/v2/closes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### closes / create

**POST** `/v2/closes`

**POST** `/v2/users/:user_id/closes`

If you want to link a community service with this close, pass it trough the `community_services_attributes` array attribute. An email is automatically sent to the user when he is assigned to a community service.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `close` | No | hash | Must be a Hash |

### closes / update

**PATCH** `/v2/closes/:id`

**PUT** `/v2/closes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `close` | No | hash | Must be a Hash |

### closes / destroy

**DELETE** `/v2/closes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `close` | No | hash | Must be a Hash |

### closes / unclose

**PATCH** `/v2/closes/:id/unclose`

**PUT** `/v2/closes/:id/unclose`

Change the close state from `close` to `unclose`.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### closes / close

**PATCH** `/v2/closes/:id/close`

**PUT** `/v2/closes/:id/close`

Change the close state from `unclose` to `close`.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## clusters

The clusters

### clusters / index

**GET** `/v2/clusters`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>campus_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>image</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>campus_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>image</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |
| `cluster` | No | hash | Must be a Hash |

### clusters / show

**GET** `/v2/clusters/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `cluster` | No | hash | Must be a Hash |

## coalitions

A [users](#coalitions>coalition is group of <a href=) competing inside of a [bloc](#blocs).

### coalitions / index

**GET** `/v2/coalitions`

**GET** `/v2/users/:user_id/coalitions`

**GET** `/v2/blocs/:bloc_id/coalitions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `bloc_id` | No | string | The bloc id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>bloc_id</code>, <code>user_id</code>, <code>name</code>, <code>image</code>, <code>slug</code>, <code>created_at</code>, <code>updated_at</code>, <code>color</code>, <code>cover</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |
| `coalition` | No | hash | Must be a Hash |

### coalitions / show

**GET** `/v2/coalitions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `coalition` | No | hash | Must be a Hash |

### coalitions / create

**POST** `/v2/coalitions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `coalition` | No | hash | Must be a Hash |

### coalitions / update

**PATCH** `/v2/coalitions/:id`

**PUT** `/v2/coalitions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `coalition` | No | hash | Must be a Hash |

## coalitions_users

[coalition](#users>Users belonging to a <a href=).

### coalitions_users / index

**GET** `/v2/coalitions/:coalition_id/coalitions_users`

**GET** `/v2/coalitions_users`

**GET** `/v2/users/:user_id/coalitions_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `coalition_id` | No | string | The coalition id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>coalition_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>this_year_score</code>, <code>this_year_score_updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>coalition_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>this_year_score</code>, <code>this_year_score_updated_at</code>, <code>this_year_score_updated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>coalition_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>this_year_score</code>, <code>this_year_score_updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |
| `coalitions_user` | No | hash | Must be a Hash |

### coalitions_users / show

**GET** `/v2/coalitions_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `coalitions_user` | No | hash | Must be a Hash |

### coalitions_users / create

**POST** `/v2/coalitions_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `coalitions_user` | No | hash | Must be a Hash |

### coalitions_users / update

**PATCH** `/v2/coalitions_users/:id`

**PUT** `/v2/coalitions_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `coalitions_user` | No | hash | Must be a Hash |

### coalitions_users / destroy

**DELETE** `/v2/coalitions_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `coalitions_user` | No | hash | Must be a Hash |

## commands

Products are sold on the intranet shop, here are commands

### commands / index

**GET** `/v2/products/:product_id/commands`

**GET** `/v2/campus/:campus_id/products/:product_id/commands`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `product_id` | No | string | The product id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>created_at</code>, <code>updated_at</code>, <code>product_id</code>, <code>user_id</code>, <code>owner_id</code>, <code>used</code>, <code>validator_id</code>, <code>validated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>created_at</code>, <code>updated_at</code>, <code>product_id</code>, <code>user_id</code>, <code>owner_id</code>, <code>used</code>, <code>validator_id</code>, <code>validated_at</code>, <code>validated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>created_at</code>, <code>updated_at</code>, <code>product_id</code>, <code>user_id</code>, <code>owner_id</code>, <code>used</code>, <code>validator_id</code>, <code>validated_at</code>. |

### commands / show

### commands / create

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `command` | No | hash | Must be a Hash |

### commands / update

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `command` | No | hash | Must be a Hash |

### commands / destroy

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `command` | No | hash | Must be a Hash |

## community_services

A task that an [user](#users) have to do for the community. Usually linked with a [close](#closes).

### community_services / graph

**GET** `/v2/community_services/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>schedule_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>close_id</code>, <code>tiger_id</code>, <code>duration</code>, <code>schedule_at</code>, <code>occupation</code>, <code>token</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>close_id</code>, <code>tiger_id</code>, <code>duration</code>, <code>schedule_at</code>, <code>occupation</code>, <code>token</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>, <code>schedule</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>close_id</code>, <code>tiger_id</code>, <code>duration</code>, <code>schedule_at</code>, <code>occupation</code>, <code>token</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>. |

### community_services / index

**GET** `/v2/closes/:close_id/community_services`

**GET** `/v2/community_services`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `close_id` | No | string | The close id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>close_id</code>, <code>tiger_id</code>, <code>duration</code>, <code>schedule_at</code>, <code>occupation</code>, <code>token</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>close_id</code>, <code>tiger_id</code>, <code>duration</code>, <code>schedule_at</code>, <code>occupation</code>, <code>token</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>, <code>schedule</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>close_id</code>, <code>tiger_id</code>, <code>duration</code>, <code>schedule_at</code>, <code>occupation</code>, <code>token</code>, <code>state</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### community_services / show

**GET** `/v2/community_services/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### community_services / validate

**PUT** `/v2/community_services/:id/validate` — Validate the given community service

**PATCH** `/v2/community_services/:id/validate` — Validate the given community service

Set the given community service state to `validated`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### community_services / invalidate

**PUT** `/v2/community_services/:id/invalidate` — Invalidate the given community service

**PATCH** `/v2/community_services/:id/invalidate` — Invalidate the given community service

Set the given community service state to `invalidated`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### community_services / create

**POST** `/v2/community_services`

*Warning*: When you use this call, we suggest that you know what you do. If you want to link a community service with this community_service, pass it trough the *closes#index* API call, with his `community_services_attributes` array attribute. An email is automatically sent to the user when he is assigned to a community service.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `community_service` | No | hash | Must be a Hash |

### community_services / update

**PATCH** `/v2/community_services/:id`

**PUT** `/v2/community_services/:id`

*Warning*: When you use this call, we suggest that you know what you do.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `community_service` | No | hash | Must be a Hash |

### community_services / destroy

**DELETE** `/v2/community_services/:id`

*Warning*: When you use this call, we suggest that you know what you do.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `community_service` | No | hash | Must be a Hash |

## companies

Companies from companies website

### companies / index

**GET** `/v2/companies`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>sector</code>, <code>other_sector</code>, <code>size</code>, <code>phone</code>, <code>address</code>, <code>zip</code>, <code>city</code>, <code>country</code>, <code>website_url</code>, <code>owner_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>latitude</code>, <code>longitude</code>, <code>siret</code>, <code>pro_id</code>, <code>owner_type</code>, <code>administrative_email</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>sector</code>, <code>other_sector</code>, <code>size</code>, <code>phone</code>, <code>address</code>, <code>zip</code>, <code>city</code>, <code>country</code>, <code>website_url</code>, <code>owner_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>latitude</code>, <code>longitude</code>, <code>siret</code>, <code>pro_id</code>, <code>owner_type</code>, <code>administrative_email</code>, <code>offer_id</code>, <code>expertise_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### companies / show

**GET** `/v2/companies/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### companies / subscribed_users

**GET** `/v2/companies/:company_id/subscribed_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `company_id` | Yes | string | The company id or slug (Must be String |
| `company` | No | hash | Must be a Hash |

### companies / internships_users

**GET** `/v2/companies/:company_id/internships_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `company_id` | Yes | string | The company id or slug (Must be String |
| `company` | No | hash | Must be a Hash |

## correction_point_historics

### correction_point_historics / index

**GET** `/v2/users/:user_id/correction_point_historics`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | Yes | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>user_data_id</code>, <code>scale_team_id</code>, <code>reason</code>, <code>sum</code>, <code>created_at</code>, <code>updated_at</code>, <code>total</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_data_id</code>, <code>scale_team_id</code>, <code>reason</code>, <code>sum</code>, <code>created_at</code>, <code>updated_at</code>, <code>total</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_data_id</code>, <code>scale_team_id</code>, <code>reason</code>, <code>sum</code>, <code>created_at</code>, <code>updated_at</code>, <code>total</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

## cursus

An educational cycle in 42

### cursus / index

**GET** `/v2/cursus`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>kind</code>, <code>restricted</code>, <code>is_subscriptable</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>kind</code>, <code>restricted</code>, <code>is_subscriptable</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>kind</code>, <code>restricted</code>, <code>is_subscriptable</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### cursus / show

**GET** `/v2/cursus/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### cursus / create

**POST** `/v2/cursus`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus` | No | hash | Must be a Hash |

### cursus / update

**PATCH** `/v2/cursus/:id`

**PUT** `/v2/cursus/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `cursus` | No | hash | Must be a Hash |

### cursus / destroy

**DELETE** `/v2/cursus/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## cursus_users

The [users](#users) wich are in a [cursus](#cursus)

### cursus_users / graph

**GET** `/v2/cursus_users/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>begin_at</code>, <code>has_coalition</code>, <code>blackholed_at</code>, <code>level</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>begin_at</code>, <code>has_coalition</code>, <code>blackholed_at</code>, <code>level</code>, <code>active</code>, <code>campus_id</code>, <code>end</code>, <code>future</code>, <code>blackholed</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>begin_at</code>, <code>has_coalition</code>, <code>blackholed_at</code>, <code>level</code>. |

### cursus_users / index

**GET** `/v2/cursus_users`

**GET** `/v2/users/:user_id/cursus_users`

**GET** `/v2/cursus/:cursus_id/cursus_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>begin_at</code>, <code>has_coalition</code>, <code>blackholed_at</code>, <code>level</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>begin_at</code>, <code>has_coalition</code>, <code>blackholed_at</code>, <code>level</code>, <code>active</code>, <code>campus_id</code>, <code>end</code>, <code>future</code>, <code>blackholed</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>cursus_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>begin_at</code>, <code>has_coalition</code>, <code>blackholed_at</code>, <code>level</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### cursus_users / show

**GET** `/v2/cursus_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### cursus_users / create

**POST** `/v2/cursus_users`

**POST** `/v2/users/:user_id/cursus_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `cursus_user` | No | hash | Must be a Hash |

### cursus_users / update

**PATCH** `/v2/cursus_users/:id`

**PUT** `/v2/cursus_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `cursus_user` | No | hash | Must be a Hash |

### cursus_users / destroy

**DELETE** `/v2/cursus_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## dashes

The [Dash](#dashs) is a short-time [project](#projects)

### dashes / graph

**GET** `/v2/dashes/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>cursus_id</code>, <code>skill_id</code>, <code>nbr_xp</code>, <code>slug</code>, <code>begin_at</code>, <code>duration</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>cursus_id</code>, <code>skill_id</code>, <code>nbr_xp</code>, <code>slug</code>, <code>begin_at</code>, <code>duration</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>, <code>future</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>cursus_id</code>, <code>skill_id</code>, <code>nbr_xp</code>, <code>slug</code>, <code>begin_at</code>, <code>duration</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |

### dashes / index

**GET** `/v2/dashes`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>cursus_id</code>, <code>skill_id</code>, <code>nbr_xp</code>, <code>slug</code>, <code>begin_at</code>, <code>duration</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>cursus_id</code>, <code>skill_id</code>, <code>nbr_xp</code>, <code>slug</code>, <code>begin_at</code>, <code>duration</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>, <code>future</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>cursus_id</code>, <code>skill_id</code>, <code>nbr_xp</code>, <code>slug</code>, <code>begin_at</code>, <code>duration</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### dashes / show

**GET** `/v2/dashes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### dashes / create

**POST** `/v2/dashes`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `dash` | No | hash | Must be a Hash |

### dashes / update

**PATCH** `/v2/dashes/:id`

**PUT** `/v2/dashes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `dash` | No | hash | Must be a Hash |

### dashes / destroy

**DELETE** `/v2/dashes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## dashes_users

The [dash](#dashes) of a [user](#users)

### dashes_users / graph

**GET** `/v2/dashes_users/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>dash_id</code>, <code>user_id</code>, <code>repo_uuid</code>, <code>repo_url</code>, <code>final_mark</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>dash_id</code>, <code>user_id</code>, <code>repo_uuid</code>, <code>repo_url</code>, <code>final_mark</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>dash_id</code>, <code>user_id</code>, <code>repo_uuid</code>, <code>repo_url</code>, <code>final_mark</code>, <code>created_at</code>, <code>updated_at</code>. |

### dashes_users / index

**GET** `/v2/dashes_users`

**GET** `/v2/dashes/:dash_id/dashes_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `dash_id` | No | string | The dash id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>dash_id</code>, <code>user_id</code>, <code>repo_uuid</code>, <code>repo_url</code>, <code>final_mark</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>dash_id</code>, <code>user_id</code>, <code>repo_uuid</code>, <code>repo_url</code>, <code>final_mark</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>dash_id</code>, <code>user_id</code>, <code>repo_uuid</code>, <code>repo_url</code>, <code>final_mark</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### dashes_users / show

**GET** `/v2/dashes_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### dashes_users / create

**POST** `/v2/dashes_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `dashes_user` | No | hash | Must be a Hash |

### dashes_users / update

**PATCH** `/v2/dashes_users/:id`

**PUT** `/v2/dashes_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `dashes_user` | No | hash | Must be a Hash |

### dashes_users / destroy

**DELETE** `/v2/dashes_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## endpoints

A endpoint for a [campus](#campus)

**TL,DR**

In order to synchronize all users between the intranet and the local storage system user for authentification (like LDAP) set on a campus, each campus must set a webservice which will be called by the intranet on a user creation / update / close / unclose. A short implementation [is available here](https://gist.github.com/lambda2/2061ee935c6170f9e748).

**Endpoints**

The following endpoints will be called on actions on users, depending on his campus, and are:

**Close**

Called when a user is closed.

`POST /users/%user/close`

Parameters:

`{
  "id":5696,
  "user_id":16814,
  "closer_id":109,
  "reason":"La raison du close",
  "state":"close",
  "created_at":"2016-01-23T14:59:22.789Z",
  "updated_at":"2016-01-23T14:59:22.789Z",
  "key"=>"a_secret_for_your_webservice"
}`

**Unclose**

Called when a user is unclosed.

`POST /users/%user/unclose`

Parameters:

`{
  "key"=>"a_secret_for_your_webservice"
}`

**Update**

Called when a user is updated.

`POST /users/%user/update`

Parameters:

`# All the user fields. If the password is changed, the new password is displayed, uncrypted.
{
  "uid":"andre",
  "login":"andre",
  "key":"a_secret_for_your_webservice",
  "id":74,
  "email":"andre@staff.42.fr",
  "password":"the_new_password",
  "created_at":"2016-01-20T00:32:50.226Z",
  "updated_at":"2016-09-16T23:36:59.971Z",
  "image_url":"/uploads/users/andre.jpg",
  "first_name":"Andre",
  "last_name":"AUBIN",
  "phone":null,
  "pool_year":null,
  "pool_month":null,
  "kind":"admin",
  "status":null,
  "campus":[
    {
      "id":1,
      "name":"Paris",
      "created_at":"2015-05-19T10:53:31.459Z",
      "updated_at":"2016-09-22T09:11:25.476Z",
      "time_zone":"Europe/Paris",
      "language_id":1,
      "slug":"paris",
      "main_email":"general@staff.42.fr",
      "endpoint_id":1,
      "vogsphere_id":1
    }
  ],
  "primary_campus":{
    "id":1,
    "name":"Paris",
    "created_at":"2015-05-19T10:53:31.459Z",
    "updated_at":"2016-09-22T09:11:25.476Z",
    "time_zone":"Europe/Paris",
    "language_id":1,
    "slug":"paris",
    "main_email":"general@staff.42.fr",
    "endpoint_id":1,
    "vogsphere_id":1
  },
  "meta":{
    "additional":"informations",
    "can_be":"set here"
  }
}`

**Create**

Called when a user is created.

`POST /users/new`

Parameters:

`# All the fields of the new user.
{
  "uid":"andre",
  "login":"andre",
  "key":"a_secret_for_your_webservice",
  "id":74,
  "email":"andre@staff.42.fr",
  "password":"the_new_password",
  "created_at":"2016-01-20T00:32:50.226Z",
  "updated_at":"2016-09-16T23:36:59.971Z",
  "image_url":"/uploads/users/andre.jpg",
  "first_name":"Andre",
  "last_name":"AUBIN",
  "phone":null,
  "pool_year":null,
  "pool_month":null,
  "kind":"admin",
  "status":null,
  "campus":[
    {
      "id":1,
      "name":"Paris",
      "created_at":"2015-05-19T10:53:31.459Z",
      "updated_at":"2016-09-22T09:11:25.476Z",
      "time_zone":"Europe/Paris",
      "language_id":1,
      "slug":"paris",
      "main_email":"general@staff.42.fr",
      "endpoint_id":1,
      "vogsphere_id":1
    }
  ],
  "primary_campus":{
    "id":1,
    "name":"Paris",
    "created_at":"2015-05-19T10:53:31.459Z",
    "updated_at":"2016-09-22T09:11:25.476Z",
    "time_zone":"Europe/Paris",
    "language_id":1,
    "slug":"paris",
    "main_email":"general@staff.42.fr",
    "endpoint_id":1,
    "vogsphere_id":1
  },
  "meta":{
    "additional":"informations",
    "can_be":"set here"
  }
}`

The `meta` user field contain additional information which can be added trough the API, like, for example, a `group_id`, and which will not be saved in the database. The uncrypted password is shown, but will not be saved in the database. So it’s the only time it will be available on user creation.

**Error handling**

The implemented webserice have to handle errors correctly, and return the good HTTP response code.

Http CodeMeaning404 (Not found)The user can’t be found
422 (Unprocessable entity)Parameters are unprocessable or missing
500 (Internal server error)Error on the webservice
200 (Ok) (or 200, 201, 204)Ok

It’s optional, but we encourage you to respond **200**, **201** and **204** for actions.

**Security and format**

Exchanges **MUST** be done over a SSL tunnel (e.g. https).

If the endpoint requires a secret token, it will be sent with the data under the `key` key.

If datas are sent, they will always be in JSON format.

**Additional data**

The `meta` user field contain additional information which can be added trough the API, like, for example, a `group_id`, and which will not be saved in the database.

**Example of implementation**

[available here](https://gist.github.com/lambda2/2061ee935c6170f9e748)

### endpoints / index

**GET** `/v2/endpoints`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>url</code>, <code>secret</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>, <code>active</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>url</code>, <code>secret</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>, <code>active</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>url</code>, <code>secret</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>, <code>active</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### endpoints / show

**GET** `/v2/endpoints/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### endpoints / create

**POST** `/v2/endpoints`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `endpoint` | No | hash | Must be a Hash |

### endpoints / update

**PATCH** `/v2/endpoints/:id`

**PUT** `/v2/endpoints/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `endpoint` | No | hash | Must be a Hash |

### endpoints / destroy

**DELETE** `/v2/endpoints/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### endpoints / callback

**POST** `/v2/endpoints/:id/callback` — Callback for an endpoint

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `url` | Yes | string | The url of the endpoint (Must be String |
| `user_id` | Yes | numeric | The user id (Must be Integer |
| `initial_data` | Yes | hash | The initial data sent to the endpoint (Must be Hash |
| `response_data` | Yes | hash | The response data from the endpoint (Must be Hash |

## evaluations

The [Evaluation](#dashs) of a [project](#projects)

### evaluations / graph

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>position</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>position</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>position</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>. |

### evaluations / index

**GET** `/v2/evaluations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>position</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>position</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>position</code>, <code>kind</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### evaluations / show

**GET** `/v2/evaluations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### evaluations / create

**POST** `/v2/evaluations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `evaluation` | No | hash | Must be a Hash |

### evaluations / update

**PATCH** `/v2/evaluations/:id`

**PUT** `/v2/evaluations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `evaluation` | No | hash | Must be a Hash |

### evaluations / destroy

**DELETE** `/v2/evaluations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## events

The events in a [campus](#campus) or a [cursus](#cursus)

### events / graph

**GET** `/v2/events/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>name</code>, <code>description</code>, <code>location</code>, <code>kind</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>prohibition_of_cancellation</code>, <code>difficulty</code>, <code>remote</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>name</code>, <code>description</code>, <code>location</code>, <code>kind</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>prohibition_of_cancellation</code>, <code>difficulty</code>, <code>remote</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>name</code>, <code>description</code>, <code>location</code>, <code>kind</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>prohibition_of_cancellation</code>, <code>difficulty</code>, <code>remote</code>. |

### events / index

**GET** `/v2/cursus/:cursus_id/events`

**GET** `/v2/campus/:campus_id/events`

**GET** `/v2/campus/:campus_id/cursus/:cursus_id/events`

**GET** `/v2/users/:user_id/events`

**GET** `/v2/events`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>name</code>, <code>description</code>, <code>location</code>, <code>kind</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>prohibition_of_cancellation</code>, <code>difficulty</code>, <code>remote</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>name</code>, <code>description</code>, <code>location</code>, <code>kind</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>prohibition_of_cancellation</code>, <code>difficulty</code>, <code>remote</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>name</code>, <code>description</code>, <code>location</code>, <code>kind</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>prohibition_of_cancellation</code>, <code>difficulty</code>, <code>remote</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### events / show

**GET** `/v2/events/:id`

Return the event specified by the `:id` parameter. Invisibles event need at least the `basic_staff` role.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### events / create

**POST** `/v2/events`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `event` | No | hash | Must be a Hash |

### events / update

**PATCH** `/v2/events/:id`

**PUT** `/v2/events/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `event` | No | hash | Must be a Hash |

### events / destroy

**DELETE** `/v2/events/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## events_users

[Users](#users) registered to an [event](#events)

### events_users / index

**GET** `/v2/users/:user_id/events_users`

**GET** `/v2/events/:event_id/events_users`

**GET** `/v2/events_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `event_id` | No | string | The event id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>event_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>event_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>event_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### events_users / show

**GET** `/v2/events_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### events_users / create

**POST** `/v2/events_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `events_user` | No | hash | Must be a Hash |

### events_users / update

**PATCH** `/v2/events_users/:id`

**PUT** `/v2/events_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `events_user` | No | hash | Must be a Hash |

### events_users / destroy

**DELETE** `/v2/events_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## exams

The exam in a [campus](#campus) or a [cursus](#cursus)

### exams / graph

**GET** `/v2/exams/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>location</code>, <code>ip_range</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>name</code>, <code>campus_id</code>, <code>validated_at</code>, <code>validator_id</code>, <code>prohibition_of_cancellation</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>location</code>, <code>ip_range</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>name</code>, <code>campus_id</code>, <code>validated_at</code>, <code>validator_id</code>, <code>prohibition_of_cancellation</code>, <code>future</code>, <code>end</code>, <code>validated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>location</code>, <code>ip_range</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>name</code>, <code>campus_id</code>, <code>validated_at</code>, <code>validator_id</code>, <code>prohibition_of_cancellation</code>. |

### exams / index

**GET** `/v2/cursus/:cursus_id/exams`

**GET** `/v2/campus/:campus_id/exams`

**GET** `/v2/campus/:campus_id/cursus/:cursus_id/exams`

**GET** `/v2/users/:user_id/exams`

**GET** `/v2/projects/:project_id/exams`

**GET** `/v2/exams`

List all visibles exams. Invisibles exams need at least the `basic_staff` role.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `project_id` | No | string | The project id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>location</code>, <code>ip_range</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>name</code>, <code>campus_id</code>, <code>validated_at</code>, <code>validator_id</code>, <code>prohibition_of_cancellation</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>location</code>, <code>ip_range</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>name</code>, <code>campus_id</code>, <code>validated_at</code>, <code>validator_id</code>, <code>prohibition_of_cancellation</code>, <code>future</code>, <code>end</code>, <code>validated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>location</code>, <code>ip_range</code>, <code>max_people</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>name</code>, <code>campus_id</code>, <code>validated_at</code>, <code>validator_id</code>, <code>prohibition_of_cancellation</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### exams / show

**GET** `/v2/exams/:id`

Return the exam specified by the `:id` parameter. Invisibles exams need at least the `basic_staff` role.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### exams / create

**POST** `/v2/exams`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `exam` | No | hash | Must be a Hash |

### exams / update

**PATCH** `/v2/exams/:id`

**PUT** `/v2/exams/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `exam` | No | hash | Must be a Hash |

### exams / destroy

**DELETE** `/v2/exams/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## exams_users

### exams_users / index

**GET** `/v2/exams/:exam_id/exams_users`

List all visibles exams_users

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `exam_id` | Yes | string | The exam id (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>exam_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>exam_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### exams_users / create

**POST** `/v2/exams/:exam_id/exams_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `exam_id` | Yes | string | The exam id (Must be String |

### exams_users / update

### exams_users / destroy

**DELETE** `/v2/exams/:exam_id/exams_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `exam_id` | Yes | string | The exam id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

## experiences

An experience gained by an [user](#users) in a particular [skill](#skills).

### experiences / index

**GET** `/v2/experiences`

**GET** `/v2/campus/:campus_id/experiences`

**GET** `/v2/projects_users/:projects_user_id/experiences`

**GET** `/v2/users/:user_id/experiences`

**GET** `/v2/skills/:skill_id/experiences`

**GET** `/v2/partnerships_users/:partnerships_user_id/experiences`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus_id` | No | string | The campus id or slug (Must be String |
| `projects_user_id` | No | string | The projects_user id (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `skill_id` | No | string | The skill id or slug (Must be String |
| `partnerships_user_id` | No | string | The partnerships_user id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>skill_id</code>, <code>experiancable_id</code>, <code>experiancable_type</code>, <code>experience</code>, <code>created_at</code>, <code>cursus_id</code>, <code>is_bonus</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>skill_id</code>, <code>experiancable_id</code>, <code>experiancable_type</code>, <code>experience</code>, <code>created_at</code>, <code>cursus_id</code>, <code>is_bonus</code>, <code>campus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>skill_id</code>, <code>experiancable_id</code>, <code>experiancable_type</code>, <code>experience</code>, <code>created_at</code>, <code>cursus_id</code>, <code>is_bonus</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### experiences / show

**GET** `/v2/experiences/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### experiences / create

**POST** `/v2/experiences`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `experience` | No | hash | Must be a Hash |

### experiences / update

**PATCH** `/v2/experiences/:id`

**PUT** `/v2/experiences/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `experience` | No | hash | Must be a Hash |

### experiences / destroy

**DELETE** `/v2/experiences/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## expertises

Pedagogic expertises

### expertises / index

**GET** `/v2/expertises`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### expertises / show

**GET** `/v2/expertises/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### expertises / create

**POST** `/v2/expertises`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `expertise` | No | hash | Must be a Hash |

### expertises / update

**PATCH** `/v2/expertises/:id`

**PUT** `/v2/expertises/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `expertise` | No | hash | Must be a Hash |

### expertises / destroy

**DELETE** `/v2/expertises/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## expertises_users

[Users](#users) which have an [expertise](#expertises)

### expertises_users / index

**GET** `/v2/expertises/:expertise_id/expertises_users`

**GET** `/v2/users/:user_id/expertises_users`

**GET** `/v2/expertises_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `expertise_id` | No | string | The expertise id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>expertise_id</code>, <code>user_id</code>, <code>interested</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>, <code>contact_me</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>expertise_id</code>, <code>user_id</code>, <code>interested</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>, <code>contact_me</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>expertise_id</code>, <code>user_id</code>, <code>interested</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>, <code>contact_me</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### expertises_users / show

**GET** `/v2/expertises_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### expertises_users / create

**POST** `/v2/expertises/:expertise_id/expertises_users`

**POST** `/v2/users/:user_id/expertises_users`

**POST** `/v2/expertises_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `expertise_id` | No | string | The expertise id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `expertises_user` | No | hash | Must be a Hash |

### expertises_users / update

**PATCH** `/v2/expertises_users/:id`

**PUT** `/v2/expertises_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `expertises_user` | No | hash | Must be a Hash |

### expertises_users / destroy

**DELETE** `/v2/expertises_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## feedbacks

The feedback of a [ScaleTeam](#scale_teams) or an [Event](#events)

### feedbacks / index

**GET** `/v2/events/:event_id/feedbacks`

**GET** `/v2/feedbacks`

**GET** `/v2/scale_teams/:scale_team_id/feedbacks`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `event_id` | No | string | The event id (Must be String |
| `scale_team_id` | No | string | The scale_team id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at asc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>feedbackable_type</code>, <code>feedbackable_id</code>, <code>comment</code>, <code>rating</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>feedbackable_type</code>, <code>feedbackable_id</code>, <code>comment</code>, <code>rating</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>feedbackable_type</code>, <code>feedbackable_id</code>, <code>comment</code>, <code>rating</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### feedbacks / show

**GET** `/v2/events/:event_id/feedbacks/:id`

**GET** `/v2/feedbacks/:id`

**GET** `/v2/scale_teams/:scale_team_id/feedbacks/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `event_id` | No | string | The event id (Must be String |
| `id` | Yes | string | The requested id (Must be String |
| `scale_team_id` | No | string | The scale_team id (Must be String |

### feedbacks / create

**POST** `/v2/events/:event_id/feedbacks`

**POST** `/v2/feedbacks`

**POST** `/v2/scale_teams/:scale_team_id/feedbacks`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `event_id` | No | string | The event id (Must be String |
| `scale_team_id` | No | string | The scale_team id (Must be String |
| `feedback` | No | hash | Must be a Hash |

### feedbacks / update

**PATCH** `/v2/events/:event_id/feedbacks/:id`

**PUT** `/v2/events/:event_id/feedbacks/:id`

**PATCH** `/v2/feedbacks/:id`

**PUT** `/v2/feedbacks/:id`

**PATCH** `/v2/scale_teams/:scale_team_id/feedbacks/:id`

**PUT** `/v2/scale_teams/:scale_team_id/feedbacks/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `event_id` | No | string | The event id (Must be String |
| `id` | Yes | string | The requested id (Must be String |
| `scale_team_id` | No | string | The scale_team id (Must be String |
| `feedback` | No | hash | Must be a Hash |

### feedbacks / destroy

**DELETE** `/v2/events/:event_id/feedbacks/:id`

**DELETE** `/v2/feedbacks/:id`

**DELETE** `/v2/scale_teams/:scale_team_id/feedbacks/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `event_id` | No | string | The event id (Must be String |
| `id` | Yes | string | The requested id (Must be String |
| `scale_team_id` | No | string | The scale_team id (Must be String |

## flags

Flags from scales

### flags / index

**GET** `/v2/flags`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by name asc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>positive</code>, <code>icon</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>positive</code>, <code>icon</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>positive</code>, <code>icon</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

## flash_users

The [Flash Users](#flash_users)

### flash_users / index

**GET** `/v2/flashes/:flash_id/flash_users`

**GET** `/v2/flash_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `flash_id` | No | string | The flash id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at asc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>flash_id</code>, <code>seen</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>flash_id</code>, <code>seen</code>, <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>end</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### flash_users / show

**GET** `/v2/flashes/:flash_id/flash_users/:id`

**GET** `/v2/flash_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `flash_id` | No | string | The flash id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### flash_users / create

**POST** `/v2/flashes/:flash_id/flash_users`

**POST** `/v2/flash_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `flash_id` | No | string | The flash id (Must be String |
| `flash_user` | No | hash | Must be a Hash |

## flashes

The [Flash](#flashes)

### flashes / index

**GET** `/v2/flashes`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at asc, id desc by default. (Must be one of: <code>id</code>, <code>content</code>, <code>selector</code>, <code>created_at</code>, <code>updated_at</code>, <code>identifier</code>, <code>title</code>, <code>url</code>, <code>duration</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>content</code>, <code>selector</code>, <code>created_at</code>, <code>updated_at</code>, <code>identifier</code>, <code>title</code>, <code>url</code>, <code>duration</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### flashes / show

**GET** `/v2/flashes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### flashes / create

**POST** `/v2/flashes`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `flash` | No | hash | Must be a Hash |

## gitlab_users

### gitlab_users / index

**GET** `/v2/users/:user_id/gitlab_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | Yes | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>public_key</code>, <code>created_at</code>, <code>updated_at</code>, <code>name</code>, <code>fingerprint</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>public_key</code>, <code>created_at</code>, <code>updated_at</code>, <code>name</code>, <code>fingerprint</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>public_key</code>, <code>created_at</code>, <code>updated_at</code>, <code>name</code>, <code>fingerprint</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

## groups

Groups in which [users](#users) belong to. It will display a label on their profile and on the forum.

### groups / index

**GET** `/v2/groups`

**GET** `/v2/users/:user_id/groups`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### groups / show

**GET** `/v2/groups/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### groups / create

**POST** `/v2/groups`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `group` | No | hash | Must be a Hash |

### groups / update

**PATCH** `/v2/groups/:id`

**PUT** `/v2/groups/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `group` | No | hash | Must be a Hash |

### groups / destroy

**DELETE** `/v2/groups/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## groups_users

[Users](#users) who are in a [group](#group).

### groups_users / index

**GET** `/v2/groups_users`

**GET** `/v2/groups/:group_id/groups_users`

**GET** `/v2/users/:user_id/groups_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `group_id` | No | string | The group id (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### groups_users / show

**GET** `/v2/groups_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### groups_users / create

**POST** `/v2/groups_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `groups_user` | No | hash | Must be a Hash |

### groups_users / update

**PATCH** `/v2/groups_users/:id`

**PUT** `/v2/groups_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `groups_user` | No | hash | Must be a Hash |

### groups_users / destroy

**DELETE** `/v2/groups_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## internships

The [internship](#internships)

### internships / index

**GET** `/v2/internships`

**GET** `/v2/users/:user_id/internships`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>administration_id</code>, <code>offer_id</code>, <code>language_id</code>, <code>state</code>, <code>days</code>, <code>user_address</code>, <code>user_postal</code>, <code>user_city</code>, <code>user_country</code>, <code>company_name</code>, <code>company_boss_user_first_name</code>, <code>company_boss_user_last_name</code>, <code>company_boss_user_email</code>, <code>company_boss_user_phone</code>, <code>company_user_first_name</code>, <code>company_user_last_name</code>, <code>company_user_post</code>, <code>company_user_email</code>, <code>company_user_phone</code>, <code>company_address</code>, <code>company_postal</code>, <code>company_city</code>, <code>company_country</code>, <code>company_siret</code>, <code>internship_address</code>, <code>internship_postal</code>, <code>internship_city</code>, <code>internship_country</code>, <code>contract_type</code>, <code>subject</code>, <code>start_at</code>, <code>end_at</code>, <code>duration</code>, <code>nb_days</code>, <code>nb_hours</code>, <code>movement</code>, <code>salary</code>, <code>currency</code>, <code>breach_at</code>, <code>convention</code>, <code>created_at</code>, <code>updated_at</code>, <code>anti_grav_units_user_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>administration_id</code>, <code>offer_id</code>, <code>language_id</code>, <code>state</code>, <code>days</code>, <code>user_address</code>, <code>user_postal</code>, <code>user_city</code>, <code>user_country</code>, <code>company_name</code>, <code>company_boss_user_first_name</code>, <code>company_boss_user_last_name</code>, <code>company_boss_user_email</code>, <code>company_boss_user_phone</code>, <code>company_user_first_name</code>, <code>company_user_last_name</code>, <code>company_user_post</code>, <code>company_user_email</code>, <code>company_user_phone</code>, <code>company_address</code>, <code>company_postal</code>, <code>company_city</code>, <code>company_country</code>, <code>company_siret</code>, <code>internship_address</code>, <code>internship_postal</code>, <code>internship_city</code>, <code>internship_country</code>, <code>contract_type</code>, <code>subject</code>, <code>start_at</code>, <code>end_at</code>, <code>duration</code>, <code>nb_days</code>, <code>nb_hours</code>, <code>movement</code>, <code>salary</code>, <code>currency</code>, <code>breach_at</code>, <code>convention</code>, <code>created_at</code>, <code>updated_at</code>, <code>anti_grav_units_user_id</code>, <code>start</code>, <code>end</code>, <code>breach</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>administration_id</code>, <code>offer_id</code>, <code>language_id</code>, <code>state</code>, <code>days</code>, <code>user_address</code>, <code>user_postal</code>, <code>user_city</code>, <code>user_country</code>, <code>company_name</code>, <code>company_boss_user_first_name</code>, <code>company_boss_user_last_name</code>, <code>company_boss_user_email</code>, <code>company_boss_user_phone</code>, <code>company_user_first_name</code>, <code>company_user_last_name</code>, <code>company_user_post</code>, <code>company_user_email</code>, <code>company_user_phone</code>, <code>company_address</code>, <code>company_postal</code>, <code>company_city</code>, <code>company_country</code>, <code>company_siret</code>, <code>internship_address</code>, <code>internship_postal</code>, <code>internship_city</code>, <code>internship_country</code>, <code>contract_type</code>, <code>subject</code>, <code>start_at</code>, <code>end_at</code>, <code>duration</code>, <code>nb_days</code>, <code>nb_hours</code>, <code>movement</code>, <code>salary</code>, <code>currency</code>, <code>breach_at</code>, <code>convention</code>, <code>created_at</code>, <code>updated_at</code>, <code>anti_grav_units_user_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### internships / create

**POST** `/v2/internships`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `internship` | No | hash | Must be a Hash |

### internships / update

**PATCH** `/v2/internships/:id`

**PUT** `/v2/internships/:id`

**PATCH** `/v2/users/:user_id/internships/:id`

**PUT** `/v2/users/:user_id/internships/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `internship` | No | hash | Must be a Hash |

### internships / show

**GET** `/v2/internships/:id`

**GET** `/v2/users/:user_id/internships/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |

### internships / destroy

**DELETE** `/v2/internships/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `internship` | No | hash | Must be a Hash |

## journals

### journals / index

**GET** `/v2/campus/:campus_id/journals`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `begin_at` | Yes | string | begin_at must be before or equal to end_at, your date range must be 124 days maximum (Must be String |
| `end_at` | Yes | string | end_at must be after or equal to begin_at, your date range must be 124 days maximum (Must be String |
| `campus_id` | Yes | string | The campus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>item_type</code>, <code>item_id</code>, <code>cursus_id</code>, <code>campus_id</code>, <code>reason</code>, <code>created_at</code>, <code>updated_at</code>, <code>event_at</code>, <code>alumni</code>, <code>closed</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>item_type</code>, <code>item_id</code>, <code>cursus_id</code>, <code>campus_id</code>, <code>reason</code>, <code>created_at</code>, <code>updated_at</code>, <code>event_at</code>, <code>alumni</code>, <code>closed</code>, <code>event</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

## languages

The [language](#languages)

### languages / graph

**GET** `/v2/languages/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>identifier</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>identifier</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>identifier</code>, <code>created_at</code>, <code>updated_at</code>. |

### languages / index

**GET** `/v2/languages`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>identifier</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>identifier</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>identifier</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### languages / show

**GET** `/v2/languages/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### languages / create

**POST** `/v2/languages`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `language` | No | hash | Must be a Hash |

### languages / update

**PATCH** `/v2/languages/:id`

**PUT** `/v2/languages/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `language` | No | hash | Must be a Hash |

### languages / destroy

**DELETE** `/v2/languages/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## languages_users

The [languages](#languages) of a [user](#users)

### languages_users / graph

**GET** `/v2/languages_users/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>language_id</code>, <code>user_id</code>, <code>position</code>, <code>created_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>language_id</code>, <code>user_id</code>, <code>position</code>, <code>created_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>language_id</code>, <code>user_id</code>, <code>position</code>, <code>created_at</code>. |

### languages_users / index

**GET** `/v2/users/:user_id/languages_users`

**GET** `/v2/languages_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>language_id</code>, <code>user_id</code>, <code>position</code>, <code>created_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>language_id</code>, <code>user_id</code>, <code>position</code>, <code>created_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>language_id</code>, <code>user_id</code>, <code>position</code>, <code>created_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### languages_users / show

**GET** `/v2/users/:user_id/languages_users/:id`

**GET** `/v2/languages_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### languages_users / create

**POST** `/v2/users/:user_id/languages_users`

**POST** `/v2/languages_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `languages_user` | No | hash | Must be a Hash |

### languages_users / update

**PATCH** `/v2/users/:user_id/languages_users/:id`

**PUT** `/v2/users/:user_id/languages_users/:id`

**PATCH** `/v2/languages_users/:id`

**PUT** `/v2/languages_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `id` | Yes | string | The requested id (Must be String |
| `languages_user` | No | hash | Must be a Hash |

### languages_users / destroy

**DELETE** `/v2/users/:user_id/languages_users/:id`

**DELETE** `/v2/languages_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `id` | Yes | string | The requested id (Must be String |

## levels

A level indicator for a [cursus](#cursus).

### levels / index

**GET** `/v2/levels`

**GET** `/v2/cursus/:cursus_id/levels`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>lvl</code>, <code>xp</code>, <code>cursus_id</code>, <code>created_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>lvl</code>, <code>xp</code>, <code>cursus_id</code>, <code>created_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>lvl</code>, <code>xp</code>, <code>cursus_id</code>, <code>created_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

## locations

The location of an user in a [campus](#campus)

### locations / graph

**GET** `/v2/locations/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `begin_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `begin_at`. (Must be one of: <code>begin_at</code>, <code>end_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>end_at</code>, <code>primary</code>, <code>host</code>, <code>campus_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>end_at</code>, <code>primary</code>, <code>host</code>, <code>campus_id</code>, <code>active</code>, <code>inactive</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>end_at</code>, <code>primary</code>, <code>host</code>, <code>campus_id</code>. |

### locations / index

**GET** `/v2/locations`

**GET** `/v2/users/:user_id/locations`

**GET** `/v2/campus/:campus_id/locations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>end_at</code>, <code>primary</code>, <code>host</code>, <code>campus_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>end_at</code>, <code>primary</code>, <code>host</code>, <code>campus_id</code>, <code>active</code>, <code>inactive</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>end_at</code>, <code>primary</code>, <code>host</code>, <code>campus_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### locations / show

**GET** `/v2/locations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### locations / create

**POST** `/v2/locations`

**POST** `/v2/users/:user_id/locations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `location` | No | hash | Must be a Hash |

### locations / update

**PATCH** `/v2/locations/:id`

**PUT** `/v2/locations/:id`

**PATCH** `/v2/users/:user_id/locations/:id`

**PUT** `/v2/users/:user_id/locations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `location` | No | hash | Must be a Hash |

### locations / destroy

**DELETE** `/v2/locations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### locations / end_all

**DELETE** `/v2/campus/:campus_id/locations/end_all` — End all locations.

Will end all locations of a given campus.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus_id` | Yes | string | The campus id or slug (Must be String |

## mailings

Mails from and between 42 entities

### mailings / index

**GET** `/v2/mailings`

**GET** `/v2/users/:user_id/mailings`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>subject</code>, <code>created_at</code>, <code>updated_at</code>, <code>identifier</code>, <code>meta</code>, <code>title</code>, <code>subtitle</code>, <code>attachment</code>, <code>from</code>, <code>to</code>, <code>cc</code>, <code>bcc</code>, <code>content</code>, <code>html_content</code>, <code>attachments</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>subject</code>, <code>created_at</code>, <code>updated_at</code>, <code>identifier</code>, <code>meta</code>, <code>title</code>, <code>subtitle</code>, <code>attachment</code>, <code>from</code>, <code>to</code>, <code>cc</code>, <code>bcc</code>, <code>content</code>, <code>html_content</code>, <code>attachments</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>subject</code>, <code>created_at</code>, <code>updated_at</code>, <code>identifier</code>, <code>meta</code>, <code>title</code>, <code>subtitle</code>, <code>attachment</code>, <code>from</code>, <code>to</code>, <code>cc</code>, <code>bcc</code>, <code>content</code>, <code>html_content</code>, <code>attachments</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### mailings / show

**GET** `/v2/mailings/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### mailings / create

**POST** `/v2/mailings` — Create a new mail

Create a new, authenticated mail, from 42.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `mailing` | No | hash | Must be a Hash |
| `at` | No | string | The time to send the mail. If none, send it now. (Must be DateTime |

### mailings / update

**PATCH** `/v2/mailings/:id`

**PUT** `/v2/mailings/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `mailing` | No | hash | Must be a Hash |
| `at` | No | string | The time to send the mail. If none, send it now. (Must be DateTime |

### mailings / destroy

**DELETE** `/v2/mailings/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## notes

A note for an [user](#users)

### notes / index

**GET** `/v2/users/:user_id/notes`

**GET** `/v2/campus/:campus_id/notes`

**GET** `/v2/notes`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>from</code>, <code>subject</code>, <code>content</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>approved_at</code>, <code>approver_id</code>, <code>from_user_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>from</code>, <code>subject</code>, <code>content</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>approved_at</code>, <code>approver_id</code>, <code>from_user_id</code>, <code>approved</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>from</code>, <code>subject</code>, <code>content</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>approved_at</code>, <code>approver_id</code>, <code>from_user_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### notes / show

**GET** `/v2/notes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### notes / create

**POST** `/v2/notes`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `note` | No | hash | Must be a Hash |

### notes / update

**PATCH** `/v2/notes/:id`

**PUT** `/v2/notes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `note` | No | hash | Must be a Hash |

### notes / destroy

**DELETE** `/v2/notes/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## notions

The elearning notion in a [cursus](#cursus)

### notions / index

**GET** `/v2/cursus/:cursus_id/notions`

**GET** `/v2/tags/:tag_id/notions`

**GET** `/v2/notions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `tag_id` | No | string | The tag id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### notions / show

**GET** `/v2/notions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### notions / create

**POST** `/v2/notions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `notion` | No | hash | Must be a Hash |

### notions / update

**PATCH** `/v2/notions/:id`

**PUT** `/v2/notions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `notion` | No | hash | Must be a Hash |

### notions / destroy

**DELETE** `/v2/notions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## offers

Offers from companies website

### offers / index

**GET** `/v2/offers`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>title</code>, <code>little_description</code>, <code>big_description</code>, <code>salary</code>, <code>contract_type</code>, <code>email</code>, <code>address</code>, <code>city</code>, <code>zip</code>, <code>country</code>, <code>latitude</code>, <code>longitude</code>, <code>valid_at</code>, <code>invalid_at</code>, <code>min_duration</code>, <code>max_duration</code>, <code>document</code>, <code>slug</code>, <code>created_at</code>, <code>updated_at</code>, <code>pro_id</code>, <code>company_id</code>, <code>target</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>title</code>, <code>little_description</code>, <code>big_description</code>, <code>salary</code>, <code>contract_type</code>, <code>email</code>, <code>address</code>, <code>city</code>, <code>zip</code>, <code>country</code>, <code>latitude</code>, <code>longitude</code>, <code>valid_at</code>, <code>invalid_at</code>, <code>min_duration</code>, <code>max_duration</code>, <code>document</code>, <code>slug</code>, <code>created_at</code>, <code>updated_at</code>, <code>pro_id</code>, <code>company_id</code>, <code>target</code>, <code>contract_type</code>, <code>target</code>, <code>expertise_id</code>, <code>campus_id</code>, <code>country</code>, <code>expertise</code>, <code>reported</code>, <code>user_id</code>, <code>valid</code>, <code>invalid</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### offers / show

**GET** `/v2/offers/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### offers / create

**POST** `/v2/offers`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `offer` | No | hash | Must be a Hash |

## offers_users

[Users](#users) who have subscribed to an [offer](#title).

### offers_users / index

**GET** `/v2/offers/:offer_id/offers_users`

**GET** `/v2/users/:user_id/offers_users`

**GET** `/v2/offers_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `offer_id` | No | string | The offer id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>offer_id</code>, <code>user_id</code>, <code>validated_at</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>offer_id</code>, <code>user_id</code>, <code>validated_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>validated</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### offers_users / show

**GET** `/v2/offers_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## params_project_sessions_rules

The value of a parameter for a [project sessions rule](#project_sessions_rules).

### params_project_sessions_rules / index

**GET** `/v2/project_sessions_rules/:project_sessions_rule_id/params_project_sessions_rules`

**GET** `/v2/params_project_sessions_rules`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_sessions_rule_id` | No | string | The project_sessions_rule id (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>param_id</code>, <code>project_sessions_rule_id</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>param_id</code>, <code>project_sessions_rule_id</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>param_id</code>, <code>project_sessions_rule_id</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### params_project_sessions_rules / show

**GET** `/v2/params_project_sessions_rules/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### params_project_sessions_rules / create

**POST** `/v2/project_sessions_rules/:project_sessions_rule_id/params_project_sessions_rules`

**POST** `/v2/params_project_sessions_rules`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_sessions_rule_id` | No | string | The project_sessions_rule id (Must be String |
| `params_project_sessions_rule` | No | hash | Must be a Hash |

### params_project_sessions_rules / update

**PATCH** `/v2/params_project_sessions_rules/:id`

**PUT** `/v2/params_project_sessions_rules/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `params_project_sessions_rule` | No | hash | Must be a Hash |

## partnerships

Pedagogic partnerships

### partnerships / index

**GET** `/v2/partnerships`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>difficulty</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>file</code>, <code>cursus_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>difficulty</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>file</code>, <code>cursus_id</code>, <code>tier</code>, <code>difficulty</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>difficulty</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>file</code>, <code>cursus_id</code>, <code>difficulty</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### partnerships / show

**GET** `/v2/partnerships/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### partnerships / create

**POST** `/v2/partnerships`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `partnership` | No | hash | Must be a Hash |

### partnerships / update

**PATCH** `/v2/partnerships/:id`

**PUT** `/v2/partnerships/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `partnership` | No | hash | Must be a Hash |

### partnerships / destroy

**DELETE** `/v2/partnerships/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## partnerships_users

[Users](#users) doing a [partnership](#partnerships)

### partnerships_users / index

**GET** `/v2/partnerships/:partnership_id/partnerships_users`

**GET** `/v2/partnerships_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `partnership_id` | No | string | The partnership id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>partnership_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>final_mark</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>partnership_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>final_mark</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>partnership_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>final_mark</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### partnerships_users / show

**GET** `/v2/partnerships_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### partnerships_users / create

**POST** `/v2/partnerships/:partnership_id/partnerships_users`

**POST** `/v2/partnerships_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `partnership_id` | No | string | The partnership id or slug (Must be String |
| `partnerships_user` | No | hash | Must be a Hash |

### partnerships_users / update

**PATCH** `/v2/partnerships_users/:id`

**PUT** `/v2/partnerships_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `partnerships_user` | No | hash | Must be a Hash |

### partnerships_users / destroy

**DELETE** `/v2/partnerships_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## patronages

A patronage between two [users](#users)

### patronages / index

**GET** `/v2/patronages`

**GET** `/v2/users/:user_id/patronages`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>godfather_id</code>, <code>ongoing</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>godfather_id</code>, <code>ongoing</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>godfather_id</code>, <code>ongoing</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### patronages / show

**GET** `/v2/patronages/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### patronages / create

**POST** `/v2/patronages`

**POST** `/v2/users/:user_id/patronages`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `patronage` | No | hash | Must be a Hash |

### patronages / update

**PATCH** `/v2/patronages/:id`

**PUT** `/v2/patronages/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `patronage` | No | hash | Must be a Hash |

### patronages / destroy

**DELETE** `/v2/patronages/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## patronages_reports

A [report](#reports) for a [patronage](#patronages)

### patronages_reports / graph

**GET** `/v2/patronages_reports/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>validated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>patronage_id</code>, <code>report_id</code>, <code>validated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>patronage_id</code>, <code>report_id</code>, <code>validated_at</code>, <code>future</code>, <code>validated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>patronage_id</code>, <code>report_id</code>, <code>validated_at</code>. |

### patronages_reports / index

**GET** `/v2/patronages_reports`

**GET** `/v2/users/:user_id/patronages_reports`

**GET** `/v2/patronages/:patronage_id/patronages_reports`

**GET** `/v2/reports/:report_id/patronages_reports`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `patronage_id` | No | string | The patronage id (Must be String |
| `report_id` | No | string | The report id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>patronage_id</code>, <code>report_id</code>, <code>validated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>patronage_id</code>, <code>report_id</code>, <code>validated_at</code>, <code>future</code>, <code>validated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>patronage_id</code>, <code>report_id</code>, <code>validated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### patronages_reports / show

**GET** `/v2/patronages_reports/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### patronages_reports / create

**POST** `/v2/patronages_reports`

**POST** `/v2/users/:user_id/patronages_reports`

**POST** `/v2/patronages/:patronage_id/patronages_reports`

**POST** `/v2/reports/:report_id/patronages_reports`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `patronage_id` | No | string | The patronage id (Must be String |
| `report_id` | No | string | The report id or slug (Must be String |
| `patronages_report` | No | hash | Must be a Hash |

### patronages_reports / update

**PATCH** `/v2/patronages_reports/:id`

**PUT** `/v2/patronages_reports/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `patronages_report` | No | hash | Must be a Hash |

### patronages_reports / destroy

**DELETE** `/v2/patronages_reports/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## pools

The [pool](#pools) of evaluation points.

### pools / index

**GET** `/v2/pools`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>current_points</code>, <code>max_points</code>, <code>created_at</code>, <code>updated_at</code>, <code>cursus_id</code>, <code>campus_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>current_points</code>, <code>max_points</code>, <code>created_at</code>, <code>updated_at</code>, <code>cursus_id</code>, <code>campus_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### pools / show

**GET** `/v2/pools/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### pools / add_points

**POST** `/v2/pools/:id/points/add`

Add points in specific pool. If number of points are bigger than max points, balance will be triggered. You are allowed to modify ONLY for your campus.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `points` | Yes | string | Number of points to be added. Points can be negative. (Must be a number. |

### pools / remove_points

**DELETE** `/v2/pools/:id/points/remove`

Remove points in specific pool. If number of points are lower than max points, balance will be disappeared. You are allowed to modify ONLY for your campus.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `points` | Yes | string | Number of points to be removed. Points are converted to **absolute values** and decremented by that point. (Must be a number. |

## products

Products are sold on the intranet shop

### products / index

**GET** `/v2/products`

**GET** `/v2/campus/:campus_id/products`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus_id` | No | string | The campus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>price</code>, <code>quantity</code>, <code>begin_at</code>, <code>end_at</code>, <code>category_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>slug</code>, <code>image</code>, <code>is_uniq</code>, <code>one_time_purchase</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>price</code>, <code>quantity</code>, <code>begin_at</code>, <code>end_at</code>, <code>category_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>slug</code>, <code>image</code>, <code>is_uniq</code>, <code>one_time_purchase</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>price</code>, <code>quantity</code>, <code>begin_at</code>, <code>end_at</code>, <code>category_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>kind</code>, <code>slug</code>, <code>image</code>, <code>is_uniq</code>, <code>one_time_purchase</code>. |

### products / show

**GET** `/v2/products/:id`

**GET** `/v2/campus/:campus_id/products/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |

### products / create

**POST** `/v2/products`

**POST** `/v2/campus/:campus_id/products`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus_id` | No | string | The campus id or slug (Must be String |
| `product` | No | hash | Must be a Hash |

### products / update

**PATCH** `/v2/products/:id`

**PUT** `/v2/products/:id`

**PATCH** `/v2/campus/:campus_id/products/:id`

**PUT** `/v2/campus/:campus_id/products/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `product` | No | hash | Must be a Hash |

### products / destroy

**DELETE** `/v2/products/:id`

**DELETE** `/v2/campus/:campus_id/products/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `product` | No | hash | Must be a Hash |

## project_data

[Project](#projects) data for the graph

### project_data / index

**GET** `/v2/project_data`

**GET** `/v2/project_sessions/:project_session_id/project_data`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>coordinates</code>, <code>created_at</code>, <code>updated_at</code>, <code>by</code>, <code>kind</code>, <code>project_session_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>coordinates</code>, <code>created_at</code>, <code>updated_at</code>, <code>by</code>, <code>kind</code>, <code>project_session_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### project_data / show

**GET** `/v2/project_data/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### project_data / create

**POST** `/v2/project_data`

### project_data / update

**PATCH** `/v2/project_data/:id`

**PUT** `/v2/project_data/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `project_data` | No | hash | Must be a Hash |

### project_data / destroy

**DELETE** `/v2/project_data/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## project_sessions

A project session defines a particular behaviour for a [project](#projects), based on the [cursus](#cursus) and / or the [campus](#campus) .

### project_sessions / graph

**GET** `/v2/projects/:project_id/project_sessions/graph(/on/:field(/by/:interval))`

**GET** `/v2/project_sessions/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>project_id</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>estimate_time</code>, <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>, <code>max_people</code>, <code>duration_days</code>, <code>terminating_after</code>, <code>solo</code>, <code>is_subscriptable</code>, <code>minimum_mark</code>, <code>team_behaviour</code>, <code>commit</code>, <code>difficulty</code>, <code>description</code>, <code>objectives</code>, <code>divisor</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>project_id</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>estimate_time</code>, <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>, <code>max_people</code>, <code>duration_days</code>, <code>terminating_after</code>, <code>solo</code>, <code>is_subscriptable</code>, <code>team_behaviour</code>, <code>difficulty</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>project_id</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>estimate_time</code>, <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>, <code>max_people</code>, <code>duration_days</code>, <code>terminating_after</code>, <code>solo</code>, <code>is_subscriptable</code>, <code>team_behaviour</code>, <code>difficulty</code>. |

### project_sessions / index

**GET** `/v2/projects/:project_id/project_sessions`

**GET** `/v2/project_sessions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_id` | No | string | The project id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>project_id</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>estimate_time</code>, <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>, <code>max_people</code>, <code>duration_days</code>, <code>terminating_after</code>, <code>solo</code>, <code>is_subscriptable</code>, <code>minimum_mark</code>, <code>team_behaviour</code>, <code>commit</code>, <code>difficulty</code>, <code>description</code>, <code>objectives</code>, <code>divisor</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>project_id</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>estimate_time</code>, <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>, <code>max_people</code>, <code>duration_days</code>, <code>terminating_after</code>, <code>solo</code>, <code>is_subscriptable</code>, <code>team_behaviour</code>, <code>difficulty</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>project_id</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>estimate_time</code>, <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>, <code>end_at</code>, <code>max_people</code>, <code>duration_days</code>, <code>terminating_after</code>, <code>solo</code>, <code>is_subscriptable</code>, <code>team_behaviour</code>, <code>difficulty</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### project_sessions / show

**GET** `/v2/project_sessions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## project_sessions_rules

A [rule](#rules) linked to a project session.

### project_sessions_rules / index

**GET** `/v2/project_sessions/:project_session_id/project_sessions_rules`

**GET** `/v2/project_sessions_rules`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>rule_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>required</code>, <code>position</code>, <code>project_session_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>rule_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>required</code>, <code>position</code>, <code>project_session_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>rule_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>required</code>, <code>position</code>, <code>project_session_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### project_sessions_rules / show

**GET** `/v2/project_sessions_rules/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### project_sessions_rules / create

**POST** `/v2/project_sessions/:project_session_id/project_sessions_rules`

**POST** `/v2/project_sessions_rules`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `project_sessions_rule` | No | hash | Must be a Hash |

### project_sessions_rules / update

**PATCH** `/v2/project_sessions_rules/:id`

**PUT** `/v2/project_sessions_rules/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `project_sessions_rule` | No | hash | Must be a Hash |

## project_sessions_skills

A [skill](#skills) linked to a project session.

### project_sessions_skills / index

**GET** `/v2/project_sessions_skills`

**GET** `/v2/project_sessions/:project_session_id/project_sessions_skills`

**GET** `/v2/skills/:skill_id/project_sessions_skills`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `skill_id` | No | string | The skill id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>project_session_id</code>, <code>skill_id</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>project_session_id</code>, <code>skill_id</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>project_session_id</code>, <code>skill_id</code>, <code>value</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### project_sessions_skills / show

**GET** `/v2/project_sessions_skills/:id`

**GET** `/v2/project_sessions/:project_session_id/project_sessions_skills/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `project_session_id` | No | string | The project_session id (Must be String |

## projects

Pedagogic projects of a [cursus](#cursus)

### projects / index

**GET** `/v2/cursus/:cursus_id/projects`

**GET** `/v2/projects/:project_id/projects`

**GET** `/v2/projects`

**GET** `/v2/me/projects`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `project_id` | No | string | The project id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by position asc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>exam</code>, <code>parent_id</code>, <code>slug</code>, <code>inherited_team</code>, <code>position</code>, <code>has_git</code>, <code>has_mark</code>, <code>repository</code>, <code>git_id</code>, <code>cached_repository_path</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>visible</code>, <code>exam</code>, <code>parent_id</code>, <code>slug</code>, <code>inherited_team</code>, <code>position</code>, <code>has_git</code>, <code>has_mark</code>, <code>description</code>, <code>repository</code>, <code>git_id</code>, <code>difficulty</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>parent_id</code>, <code>slug</code>, <code>position</code>, <code>description</code>, <code>difficulty</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### projects / show

**GET** `/v2/projects/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### projects / create

**POST** `/v2/projects`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project` | No | hash | Must be a Hash |

### projects / update

**PATCH** `/v2/projects/:id`

**PUT** `/v2/projects/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `project` | No | hash | Must be a Hash |

### projects / destroy

**DELETE** `/v2/projects/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### projects / retry

**PATCH** `/v2/projects/:id/retry` — Retry the project user for the current resource owner

**PUT** `/v2/projects/:id/retry` — Retry the project user for the current resource owner

## projects_users

[Users](#users) which did or are doing a [project](#projects)

The ProjectsUser represents a user’s subscription to a project. A subscribed user can have one team or more based on his number of attempts to this project. Be careful to always select the active team (the last team).

Here are basically the different states a user can have on a project:

- He (the user) doesn’t have a projects_user, he is **not registered** on the project.

- He has no team, he is actually **searching a group**, in order to create one.

- He has a team, which is not locked (the `locked_at` field is not null), he is **creating a group**.

If the user has a locked team, then either he did, or he is doing the project. At this point, the available states are:

- His team is closed and has a final_mark (the `locked_at`, `closed_at` and `final_mark` fields aren’t null), he has **finished** his project. If he doesn’t have a final_mark yet, he his **waiting for evaluation**.

- His team is not closed yet (and obviously doesn’t have a final mark), he is **in progress**.

Some exceptional cases happen when a project has children (like piscines), or begins at a specific time (like rushes).

- The team is locked, but the project has a `begin_at` field which starts is in the future, so he his **waiting to start**.

- The team is locked, but the project has children. In this case, look at the teams on the child projects, and consider this one **in progress**.

### projects_users / graph

**GET** `/v2/projects/:project_id/projects_users/graph(/on/:field(/by/:interval))`

**GET** `/v2/users/:user_id/projects_users/graph(/on/:field(/by/:interval))`

**GET** `/v2/projects_users/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>retriable_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>project_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>occurrence</code>, <code>final_mark</code>, <code>retriable_at</code>, <code>marked_at</code>, <code>status</code>, <code>cursus</code>, <code>campus</code>, <code>retriable</code>, <code>marked</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>project_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>occurrence</code>, <code>final_mark</code>, <code>retriable_at</code>, <code>marked_at</code>, <code>status</code>. |

### projects_users / index

**GET** `/v2/projects/:project_id/projects_users`

**GET** `/v2/users/:user_id/projects_users`

**GET** `/v2/projects_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_id` | No | string | The project id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>project_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>occurrence</code>, <code>final_mark</code>, <code>retriable_at</code>, <code>marked_at</code>, <code>status</code>, <code>cursus</code>, <code>campus</code>, <code>retriable</code>, <code>marked</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>project_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>occurrence</code>, <code>final_mark</code>, <code>retriable_at</code>, <code>marked_at</code>, <code>status</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### projects_users / show

**GET** `/v2/projects_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### projects_users / create

**POST** `/v2/projects/:project_id/projects_users`

**POST** `/v2/users/:user_id/projects_users`

**POST** `/v2/projects_users`

**POST** `/v2/projects/:project_id/register`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_id` | No | string | The project id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `projects_user` | No | hash | Must be a Hash |

### projects_users / update

**PATCH** `/v2/projects_users/:id`

**PUT** `/v2/projects_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `projects_user` | No | hash | Must be a Hash |

### projects_users / destroy

**DELETE** `/v2/projects_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### projects_users / compile

**PATCH** `/v2/projects_users/:id/compile` — Compile a projects user

**PUT** `/v2/projects_users/:id/compile` — Compile a projects user

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_users_id` | Yes | numeric | The projects_user id (Must be Fixnum |

### projects_users / retry

**PATCH** `/v2/projects_users/:id/retry` — Retry a projects user

**PUT** `/v2/projects_users/:id/retry` — Retry a projects user

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | numeric | The projects_user id (Must be Fixnum |
| `force` | No | string | Will force the retry if true (Must be one of: <code>true</code>, <code>false</code>. |

### projects_users / register_childs_and_scales

**POST** `/v2/projects_users/register_childs_and_scales`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `scales` | No | hash | The scales to apply to the sub projects (Must be Hash |
| `projects_user` | No | hash | Must be a Hash |

### projects_users / reset

**DELETE** `/v2/projects_users/reset`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | Yes | numeric | The user id (Must be Fixnum |
| `project_id` | Yes | numeric | The project id (Must be Fixnum |

### projects_users / scale

**PATCH** `/v2/projects_users/scale`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | Yes | numeric | The user id (Must be Fixnum |
| `project_id` | Yes | numeric | The project id (Must be Fixnum |
| `scale` | Yes | numeric | The scale to apply to the project (Must be Fixnum |

## quests

Quests which can or must be done by [users](#users)

### quests / index

**GET** `/v2/quests`

**GET** `/v2/cursus/:cursus_id/quests`

**GET** `/v2/campus/:campus_id/quests`

**GET** `/v2/users/:user_id/quests`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>kind</code>, <code>internal_name</code>, <code>duration</code>, <code>ancestry</code>, <code>description</code>, <code>guild_size</code>, <code>guild_prct</code>, <code>cursus_id</code>, <code>campus_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>grade_id</code>, <code>position</code>, <code>mails</code>, <code>certificate_id</code>, <code>unlock_all_projects</code>, <code>tries_number</code>, <code>success_number</code>, <code>close_on_fail</code>, <code>mails_from</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>kind</code>, <code>internal_name</code>, <code>description</code>, <code>cursus_id</code>, <code>campus_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>grade_id</code>, <code>position</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>slug</code>, <code>kind</code>, <code>internal_name</code>, <code>description</code>, <code>cursus_id</code>, <code>campus_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>grade_id</code>, <code>position</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### quests / show

**GET** `/v2/quests/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### quests / create

**POST** `/v2/quests`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `quest` | No | hash | Must be a Hash |

### quests / update

**PATCH** `/v2/quests/:id`

**PUT** `/v2/quests/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `quest` | No | hash | Must be a Hash |

### quests / destroy

**DELETE** `/v2/quests/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## quests_users

[Users](#users) which earned an [quest](#quest)

### quests_users / graph

**GET** `/v2/quests_users/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>end_at</code>, <code>validated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>quest_id</code>, <code>user_id</code>, <code>end_at</code>, <code>validated_at</code>, <code>prct</code>, <code>advancement</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>quest_id</code>, <code>user_id</code>, <code>end_at</code>, <code>validated_at</code>, <code>prct</code>, <code>advancement</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>, <code>end</code>, <code>validated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>quest_id</code>, <code>user_id</code>, <code>end_at</code>, <code>validated_at</code>, <code>prct</code>, <code>advancement</code>, <code>created_at</code>, <code>updated_at</code>. |

### quests_users / index

**GET** `/v2/quests/:quest_id/quests_users`

**GET** `/v2/users/:user_id/quests_users`

**GET** `/v2/quests_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `quest_id` | No | string | The quest id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>quest_id</code>, <code>user_id</code>, <code>end_at</code>, <code>validated_at</code>, <code>prct</code>, <code>advancement</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>quest_id</code>, <code>user_id</code>, <code>end_at</code>, <code>validated_at</code>, <code>prct</code>, <code>advancement</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>, <code>end</code>, <code>validated</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>quest_id</code>, <code>user_id</code>, <code>end_at</code>, <code>validated_at</code>, <code>prct</code>, <code>advancement</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### quests_users / show

**GET** `/v2/quests_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### quests_users / create

**POST** `/v2/quests_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `quests_user` | No | hash | Must be a Hash |

### quests_users / update

**PATCH** `/v2/quests_users/:id`

**PUT** `/v2/quests_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `quests_user` | No | hash | Must be a Hash |

### quests_users / destroy

**DELETE** `/v2/quests_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## roles

Grants particular privileges to entities like [users](#users) and [applications](#apps)

### roles / index

**GET** `/v2/roles`

**GET** `/v2/users/:user_id/roles`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### roles / show

**GET** `/v2/roles/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### roles / create

**POST** `/v2/roles`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `role` | No | hash | Must be a Hash |

### roles / update

**PATCH** `/v2/roles/:id`

**PUT** `/v2/roles/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `role` | No | hash | Must be a Hash |

### roles / destroy

**DELETE** `/v2/roles/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## roles_entities

The [applications](#apps) linked to a role

### roles_entities / graph

**GET** `/v2/roles_entities/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>expires_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>role_id</code>, <code>entity_id</code>, <code>expires_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>entity_type</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>role_id</code>, <code>entity_id</code>, <code>expires_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>entity_type</code>, <code>expires</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>role_id</code>, <code>entity_id</code>, <code>expires_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>entity_type</code>. |

### roles_entities / index

**GET** `/v2/roles/:role_id/roles_entities`

**GET** `/v2/roles_entities`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `role_id` | No | string | The role id (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>role_id</code>, <code>entity_id</code>, <code>expires_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>entity_type</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>role_id</code>, <code>entity_id</code>, <code>expires_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>entity_type</code>, <code>expires</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>role_id</code>, <code>entity_id</code>, <code>expires_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>entity_type</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### roles_entities / show

**GET** `/v2/roles_entities/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### roles_entities / create

**POST** `/v2/roles_entities`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `roles_entity` | No | hash | Must be a Hash |

### roles_entities / update

**PATCH** `/v2/roles_entities/:id`

**PUT** `/v2/roles_entities/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `roles_entity` | No | hash | Must be a Hash |

### roles_entities / destroy

**DELETE** `/v2/roles_entities/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## rules

A rule for a [project](#projects)

### rules / index

**GET** `/v2/rules`

**GET** `/v2/project_sessions/:project_session_id/rules`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>kind</code>, <code>name</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>internal_name</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>kind</code>, <code>name</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>internal_name</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>kind</code>, <code>name</code>, <code>description</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>internal_name</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### rules / show

**GET** `/v2/rules/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### rules / create

**POST** `/v2/rules`

**POST** `/v2/project_sessions/:project_session_id/rules`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `rule` | No | hash | Must be a Hash |

### rules / update

**PATCH** `/v2/rules/:id`

**PUT** `/v2/rules/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `rule` | No | hash | Must be a Hash |

### rules / destroy

**DELETE** `/v2/rules/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## scale_teams

A defence of a [team](#teams) (on a [project](#projects)), involving an evaluator

### scale_teams / graph

**GET** `/v2/scale_teams/graph(/on/:field(/by/:interval))`

**GET** `/v2/projects/:project_id/scale_teams/graph(/on/:field(/by/:interval))`

**GET** `/v2/users/:user_id/scale_teams/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>begin_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>scale_id</code>, <code>team_id</code>, <code>comment</code>, <code>old_feedback</code>, <code>feedback_rating</code>, <code>final_mark</code>, <code>truant_id</code>, <code>flag_id</code>, <code>token</code>, <code>ip</code>, <code>internship_id</code>, <code>filled_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>scale_id</code>, <code>team_id</code>, <code>comment</code>, <code>old_feedback</code>, <code>feedback_rating</code>, <code>final_mark</code>, <code>truant_id</code>, <code>flag_id</code>, <code>token</code>, <code>ip</code>, <code>internship_id</code>, <code>filled_at</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>feedback_rating</code>, <code>future</code>, <code>filled</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>scale_id</code>, <code>team_id</code>, <code>comment</code>, <code>old_feedback</code>, <code>feedback_rating</code>, <code>final_mark</code>, <code>truant_id</code>, <code>flag_id</code>, <code>token</code>, <code>ip</code>, <code>internship_id</code>, <code>filled_at</code>. |

### scale_teams / index

**GET** `/v2/project_sessions/:project_session_id/scale_teams`

**GET** `/v2/scale_teams`

**GET** `/v2/projects/:project_id/scale_teams`

**GET** `/v2/users/:user_id/scale_teams/as_corrector`

**GET** `/v2/users/:user_id/scale_teams/as_corrected`

**GET** `/v2/users/:user_id/scale_teams`

**GET** `/v2/me/scale_teams/as_corrector`

**GET** `/v2/me/scale_teams/as_corrected`

**GET** `/v2/me/scale_teams`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `project_id` | No | string | The project id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by begin_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>scale_id</code>, <code>team_id</code>, <code>comment</code>, <code>old_feedback</code>, <code>feedback_rating</code>, <code>final_mark</code>, <code>truant_id</code>, <code>flag_id</code>, <code>token</code>, <code>ip</code>, <code>internship_id</code>, <code>filled_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>scale_id</code>, <code>team_id</code>, <code>comment</code>, <code>old_feedback</code>, <code>feedback_rating</code>, <code>final_mark</code>, <code>truant_id</code>, <code>flag_id</code>, <code>token</code>, <code>ip</code>, <code>internship_id</code>, <code>filled_at</code>, <code>campus_id</code>, <code>cursus_id</code>, <code>feedback_rating</code>, <code>future</code>, <code>filled</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>begin_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>scale_id</code>, <code>team_id</code>, <code>comment</code>, <code>old_feedback</code>, <code>feedback_rating</code>, <code>final_mark</code>, <code>truant_id</code>, <code>flag_id</code>, <code>token</code>, <code>ip</code>, <code>internship_id</code>, <code>filled_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### scale_teams / show

**GET** `/v2/project_sessions/:project_session_id/scale_teams/:id`

**GET** `/v2/scale_teams/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### scale_teams / create

**POST** `/v2/project_sessions/:project_session_id/scale_teams`

**POST** `/v2/scale_teams`

With this call, the evaluator is set as the token’s user_id. If you want to set an evaluation for a particular user, use the [multiple_create](/apidoc/2.0/scale_teams/multiple_create.html) call

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `scale_team` | No | hash | Must be a Hash |

### scale_teams / update

**PATCH** `/v2/project_sessions/:project_session_id/scale_teams/:id`

**PUT** `/v2/project_sessions/:project_session_id/scale_teams/:id`

**PATCH** `/v2/scale_teams/:id`

**PUT** `/v2/scale_teams/:id`

The final_mark of the scale_team is calculated automatically from the answers values. If you want to patch the mark of a project for a student, patching the `team.final_mark` is the right way to do. It will recompile the `project_user.final_mark`. If you really want to update the final_mark of the scale_team, you need to patch the `answers_attributes`.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `id` | Yes | string | The requested id (Must be String |
| `scale_team` | No | hash | Must be a Hash |

### scale_teams / destroy

**DELETE** `/v2/project_sessions/:project_session_id/scale_teams/:id`

**DELETE** `/v2/scale_teams/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### scale_teams / multiple_create

**POST** `/v2/scale_teams/multiple_create`

This calls allow the creation of one or multiple `scale_teams` in a single call. Creating a new scale_team without an `user_id` and with a `final_mark` will act as a *moulinette* mark. To be more comfortable, and for readability, we recommend that you send the data as an array of JSON objects.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `scale_teams` | No | array | Must be an Array of nested elements |

## scales

A scale is composed by questions which allows an [users](#users) to rate the quality of a [project](#projects) .

### scales / index

**GET** `/v2/project_sessions/:project_session_id/scales`

**GET** `/v2/scales`

**GET** `/v2/projects/:project_id/scales`

**GET** `/v2/users/:user_id/scales`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_session_id` | No | string | The project_session id (Must be String |
| `project_id` | No | string | The project id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by name asc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>comment</code>, <code>introduction_md</code>, <code>disclaimer_md</code>, <code>guidelines_md</code>, <code>created_at</code>, <code>updated_at</code>, <code>evaluation_id</code>, <code>is_primary</code>, <code>correction_number</code>, <code>duration</code>, <code>manual_subscription</code>, <code>is_external</code>, <code>free</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>comment</code>, <code>introduction_md</code>, <code>disclaimer_md</code>, <code>guidelines_md</code>, <code>created_at</code>, <code>updated_at</code>, <code>evaluation_id</code>, <code>is_primary</code>, <code>correction_number</code>, <code>duration</code>, <code>manual_subscription</code>, <code>is_external</code>, <code>free</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>comment</code>, <code>introduction_md</code>, <code>disclaimer_md</code>, <code>guidelines_md</code>, <code>created_at</code>, <code>updated_at</code>, <code>evaluation_id</code>, <code>is_primary</code>, <code>correction_number</code>, <code>duration</code>, <code>manual_subscription</code>, <code>is_external</code>, <code>free</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### scales / show

**GET** `/v2/scales/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### scales / create

**POST** `/v2/scales`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `scale` | No | hash | Must be a Hash |

### scales / update

**PATCH** `/v2/scales/:id`

**PUT** `/v2/scales/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `scale` | No | hash | Must be a Hash |

### scales / destroy

**DELETE** `/v2/scales/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## scores

Points given to a [coalition](#coalitions).

### scores / index

**GET** `/v2/scores`

**GET** `/v2/coalitions/:coalition_id/scores`

**GET** `/v2/coalitions_users/:coalitions_user_id/scores`

**GET** `/v2/blocs/:bloc_id/scores`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `coalition_id` | No | string | The coalition id or slug (Must be String |
| `coalitions_user_id` | No | string | The coalitions_user id (Must be String |
| `bloc_id` | No | string | The bloc id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>coalitions_user_id</code>, <code>calculation_id</code>, <code>reason</code>, <code>created_at</code>, <code>updated_at</code>, <code>coalition_id</code>, <code>scoreable_id</code>, <code>scoreable_type</code>, <code>value</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### scores / show

**GET** `/v2/scores/:id`

**GET** `/v2/coalitions/:coalition_id/scores/:id`

**GET** `/v2/coalitions_users/:coalitions_user_id/scores/:id`

**GET** `/v2/blocs/:bloc_id/scores/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `coalition_id` | No | string | The coalition id or slug (Must be String |
| `coalitions_user_id` | No | string | The coalitions_user id (Must be String |
| `bloc_id` | No | string | The bloc id (Must be String |

### scores / create

**POST** `/v2/coalitions/:coalition_id/scores`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `coalition_id` | Yes | string | The coalition id or slug (Must be String |

### scores / destroy

**DELETE** `/v2/coalitions/:coalition_id/scores/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `coalition_id` | Yes | string | The coalition id or slug (Must be String |
| `id` | Yes | string | The requested id (Must be String |

## skills

A particlar skill.

### skills / index

**GET** `/v2/skills`

**GET** `/v2/cursus/:cursus_id/skills`

**GET** `/v2/skills`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by name asc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### skills / show

**GET** `/v2/skills/:id`

**GET** `/v2/skills/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### skills / create

**POST** `/v2/skills`

**POST** `/v2/skills`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `skill` | No | hash | Must be a Hash |

### skills / update

**PATCH** `/v2/skills/:id`

**PUT** `/v2/skills/:id`

**PATCH** `/v2/skills/:id`

**PUT** `/v2/skills/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `skill` | No | hash | Must be a Hash |

### skills / destroy

**DELETE** `/v2/skills/:id`

**DELETE** `/v2/skills/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## slots

The slots available to [users](#users) for booking a [project](#projects) [scale team](#scale_teams).

A Slot is a time interval when a user desclares himself available to evaluate other users. Actually, a slot must be at least 1800 minutes by default (with a granularity of 15 minutes). Campus can manage and edit the minimum slot duration. A slot can be set every day between 30 minutes and 2 weeks in advance.

### slots / graph

**GET** `/v2/slots/graph(/on/:field(/by/:interval))`

**GET** `/v2/projects/:project_id/slots/graph(/on/:field(/by/:interval))`

**GET** `/v2/users/:user_id/slots/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>begin_at</code>, <code>end_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>user_id</code>, <code>created_at</code>, <code>scale_team_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>created_at</code>, <code>campus_id</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>created_at</code>. |

### slots / index

**GET** `/v2/slots`

**GET** `/v2/projects/:project_id/slots`

**GET** `/v2/users/:user_id/slots`

**GET** `/v2/me/slots`

A Slot is a time interval when a user desclares himself available to evaluate other users. Actually, a slot must be at least 1800 minutes by default (with a granularity of 15 minutes). Campus can manage and edit the minimum slot duration. A slot can be set every day between 30 minutes and 2 weeks in advance.

This call obviously lists all slots.

An user without the `advanced tutor` role can’t set the `user_id` or the `scale_team_id` parameter.

- 
**if there is a resource owner** (an user uses this api trough your app, with the [web application flow](http://api.intra.42.fr/apidoc/guides/web_application_flow)):

The `/me/slots` endpoint will list all the slots set by the current user.

- The `/projects/:project_id/slots` endpoint will list all the available slots for the given project. Theses slots can be booked by the current user in order to make a defense.

- 
**if there isn’t a resource owner**

The `/projects/:project_id/slots` endpoint lists all the slots scheduled (with a `scale_team`) on this project, including all the past ones.

- The `/users/:user_id/slots` endpoint lists all the slots for the requested user, as evaluator and as evaluated. This call is restricted.

In all the cases, the `/slots` endpoint lists all the slots, booked or not, including all the past ones.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_id` | No | string | The project id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>user_id</code>, <code>created_at</code>, <code>scale_team_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>created_at</code>, <code>campus_id</code>, <code>future</code>, <code>end</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>begin_at</code>, <code>end_at</code>, <code>created_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### slots / show

**GET** `/v2/slots/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### slots / create

**POST** `/v2/slots`

A Slot is a time interval when a user desclares himself available to evaluate other users. Actually, a slot must be at least 1800 minutes by default (with a granularity of 15 minutes). Campus can manage and edit the minimum slot duration. A slot can be set every day between 30 minutes and 2 weeks in advance.

An user without the `advanced tutor` role can’t set the `user_id` or the `scale_team_id` parameter.

**An app without resource owner cannot make this call**.

If there is a resource owner, the `user_id` parameter must be set to his id. The date intervals are automaticaly scaled to a 15 minutes granularity. If the duration exceeds 15 minutes, multiple slots will be created.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `slot` | No | hash | Must be a Hash |

### slots / update

**PATCH** `/v2/slots/:id`

**PUT** `/v2/slots/:id`

A Slot is a time interval when a user desclares himself available to evaluate other users. Actually, a slot must be at least 1800 minutes by default (with a granularity of 15 minutes). Campus can manage and edit the minimum slot duration. A slot can be set every day between 30 minutes and 2 weeks in advance.

An user without the `advanced tutor` role can’t set the `user_id` or the `scale_team_id` parameter.

**An app without resource owner cannot make this call**.

If there is a resource owner, the `user_id` parameter must be set to his id. The date intervals are automaticaly scaled to a 15 minutes granularity. If the duration exceeds 15 minutes, multiple slots will be created.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `slot` | No | hash | Must be a Hash |

### slots / destroy

**DELETE** `/v2/slots/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## squads

A [squads](#squads) is the managing container of [squads_users](#squads_users).

### squads / create

**POST** `/v2/blocs/:bloc_id/squads`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | Yes | string | The bloc id (Must be String |
| `squad` | No | hash | Must be a Hash |

### squads / destroy

**DELETE** `/v2/blocs/:bloc_id/squads/:id`

**DELETE** `/v2/squads/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | No | string | The bloc id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### squads / index

**GET** `/v2/blocs/:bloc_id/squads`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | Yes | string | The bloc id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>bloc_id</code>, <code>locked_at</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>bloc_id</code>, <code>locked_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>locked</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### squads / show

**GET** `/v2/blocs/:bloc_id/squads/:id`

**GET** `/v2/squads/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | No | string | The bloc id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### squads / update

**PATCH** `/v2/squads/:id`

**PUT** `/v2/squads/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## squads_users

A [squads_users](#squads_users) will group users inside a same coalition

### squads_users / create

**POST** `/v2/blocs/:bloc_id/squads_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | Yes | string | The bloc id (Must be String |

### squads_users / destroy

**DELETE** `/v2/blocs/:bloc_id/squads_users/:id`

**DELETE** `/v2/squads_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | No | string | The bloc id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### squads_users / index

**GET** `/v2/blocs/:bloc_id/squads_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `bloc_id` | Yes | string | The bloc id (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>squad_id</code>, <code>user_id</code>, <code>leader</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>squad_id</code>, <code>user_id</code>, <code>leader</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### squads_users / update

**PATCH** `/v2/squads_users/:id`

**PUT** `/v2/squads_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## subnotions

The elearning subnotion in a [notion](#notions)

### subnotions / index

**GET** `/v2/notions/:notion_id/subnotions`

**GET** `/v2/subnotions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `notion_id` | No | string | The notion id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by name asc, id desc by default. (Must be one of: <code>id</code>, <code>notion_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>position</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>notion_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>position</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>notion_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>slug</code>, <code>position</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### subnotions / show

**GET** `/v2/subnotions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### subnotions / create

**POST** `/v2/subnotions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `subnotion` | No | hash | Must be a Hash |

### subnotions / update

**PATCH** `/v2/subnotions/:id`

**PUT** `/v2/subnotions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `subnotion` | No | hash | Must be a Hash |

### subnotions / destroy

**DELETE** `/v2/subnotions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## tags

Non-hierarchical keyword, acting as a meta-data and helping to describe entities.

### tags / index

**GET** `/v2/projects/:project_id/tags`

**GET** `/v2/issues/:issue_id/tags`

**GET** `/v2/notions/:notion_id/tags`

**GET** `/v2/cursus/:cursus_id/tags`

**GET** `/v2/users/:user_id/tags`

**GET** `/v2/tags`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `project_id` | No | string | The project id or slug (Must be String |
| `issue_id` | No | string | The issue id (Must be String |
| `notion_id` | No | string | The notion id or slug (Must be String |
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by name asc, id desc by default. (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>pinner_id</code>, <code>kind</code>, <code>description</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>pinner_id</code>, <code>kind</code>, <code>description</code>, <code>cursus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>pinner_id</code>, <code>kind</code>, <code>description</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### tags / show

**GET** `/v2/tags/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### tags / create

**POST** `/v2/tags`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `tag` | No | hash | Must be a Hash |

### tags / update

**PATCH** `/v2/tags/:id`

**PUT** `/v2/tags/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `tag` | No | hash | Must be a Hash |

### tags / destroy

**DELETE** `/v2/tags/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## tags_users

Resource associating a [User](#users) and a [Tag](#tags).

### tags_users / index

**GET** `/v2/tags_users`

**GET** `/v2/users/:user_id/tags_users`

**GET** `/v2/cursus/:cursus_id/tags_users`

**GET** `/v2/campus/:campus_id/tags_users`

**GET** `/v2/tags/:tag_id/tags_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `tag_id` | No | string | The tag id (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>tag_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>tag_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>, <code>cursus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>tag_id</code>, <code>user_id</code>, <code>created_at</code>, <code>updated_at</code>, <code>campus_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### tags_users / show

**GET** `/v2/tags_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### tags_users / create

**POST** `/v2/tags_users`

### tags_users / update

**PATCH** `/v2/tags_users/:id`

**PUT** `/v2/tags_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### tags_users / destroy

**DELETE** `/v2/tags_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## teams

One or many [users](#users) which have to finish a [project](#projects) together.

### teams / graph

**GET** `/v2/cursus/:cursus_id/teams/graph(/on/:field(/by/:interval))`

**GET** `/v2/users/:user_id/teams/graph(/on/:field(/by/:interval))`

**GET** `/v2/users/:user_id/projects/:project_id/teams/graph(/on/:field(/by/:interval))`

**GET** `/v2/teams/graph(/on/:field(/by/:interval))`

**GET** `/v2/projects/:project_id/teams/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>, <code>locked_at</code>, <code>closed_at</code>, <code>deadline_at</code>, <code>terminating_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>project_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>locked_at</code>, <code>closed_at</code>, <code>final_mark</code>, <code>repo_url</code>, <code>repo_uuid</code>, <code>deadline_at</code>, <code>terminating_at</code>, <code>project_session_id</code>, <code>status</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>project_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>locked_at</code>, <code>closed_at</code>, <code>final_mark</code>, <code>repo_url</code>, <code>repo_uuid</code>, <code>deadline_at</code>, <code>terminating_at</code>, <code>project_session_id</code>, <code>status</code>, <code>cursus</code>, <code>active_cursus</code>, <code>campus</code>, <code>primary_campus</code>, <code>locked</code>, <code>closed</code>, <code>deadline</code>, <code>terminating</code>, <code>with_mark</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>project_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>locked_at</code>, <code>closed_at</code>, <code>final_mark</code>, <code>repo_url</code>, <code>repo_uuid</code>, <code>deadline_at</code>, <code>terminating_at</code>, <code>project_session_id</code>, <code>status</code>. |

### teams / index

**GET** `/v2/cursus/:cursus_id/teams`

**GET** `/v2/users/:user_id/teams`

**GET** `/v2/users/:user_id/projects/:project_id/teams`

**GET** `/v2/teams`

**GET** `/v2/projects/:project_id/teams`

**GET** `/v2/project_sessions/:project_session_id/teams`

**GET** `/v2/me/teams`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `project_id` | No | string | The project id or slug (Must be String |
| `project_session_id` | No | string | The project_session id (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>project_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>locked_at</code>, <code>closed_at</code>, <code>final_mark</code>, <code>repo_url</code>, <code>repo_uuid</code>, <code>deadline_at</code>, <code>terminating_at</code>, <code>project_session_id</code>, <code>status</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>project_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>locked_at</code>, <code>closed_at</code>, <code>final_mark</code>, <code>repo_url</code>, <code>repo_uuid</code>, <code>deadline_at</code>, <code>terminating_at</code>, <code>project_session_id</code>, <code>status</code>, <code>cursus</code>, <code>active_cursus</code>, <code>campus</code>, <code>primary_campus</code>, <code>locked</code>, <code>closed</code>, <code>deadline</code>, <code>terminating</code>, <code>with_mark</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>project_id</code>, <code>name</code>, <code>created_at</code>, <code>updated_at</code>, <code>locked_at</code>, <code>closed_at</code>, <code>final_mark</code>, <code>repo_url</code>, <code>repo_uuid</code>, <code>deadline_at</code>, <code>terminating_at</code>, <code>project_session_id</code>, <code>status</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### teams / show

**GET** `/v2/teams/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### teams / create

**POST** `/v2/teams`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `team` | No | hash | Must be a Hash |

### teams / update

**PATCH** `/v2/teams/:id`

**PUT** `/v2/teams/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `team` | No | hash | Must be a Hash |

### teams / destroy

**DELETE** `/v2/teams/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### teams / reset_team_uploads

**POST** `/v2/teams/:id/reset_team_uploads`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## teams_uploads

An uploaded mark for a [team](#teams), given by a bot (like the Moulinette), without any defence.

### teams_uploads / index

**GET** `/v2/teams/:team_id/teams_uploads`

**GET** `/v2/teams_uploads`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `team_id` | No | string | The team id (Must be String |
| `sort` | No | string | The sort field. Sorted by id asc by default. (Must be one of: <code>id</code>, <code>team_id</code>, <code>upload_id</code>, <code>final_mark</code>, <code>comment</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>team_id</code>, <code>upload_id</code>, <code>final_mark</code>, <code>comment</code>, <code>created_at</code>, <code>updated_at</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>team_id</code>, <code>upload_id</code>, <code>final_mark</code>, <code>comment</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### teams_uploads / show

**GET** `/v2/teams_uploads/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### teams_uploads / create

**POST** `/v2/teams_uploads`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `teams_upload` | No | hash | Must be a Hash |

### teams_uploads / update

**PATCH** `/v2/teams_uploads/:id`

**PUT** `/v2/teams_uploads/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `teams_upload` | No | hash | Must be a Hash |

### teams_uploads / destroy

**DELETE** `/v2/teams_uploads/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### teams_uploads / multiple_create

**POST** `/v2/teams_uploads/multiple_create` — Create multiple teams uploads

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `teams_uploads` | No | array | An array of teams_uploads (Must be an Array of nested elements |

## teams_users

[Team](#teams) composed of one [User](#users)

### teams_users / index

**GET** `/v2/teams_users`

**GET** `/v2/users/:user_id/teams_users`

**GET** `/v2/teams/:team_id/teams_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `team_id` | No | string | The team id (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>team_id</code>, <code>user_id</code>, <code>leader</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>, <code>occurrence</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>team_id</code>, <code>user_id</code>, <code>leader</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>, <code>occurrence</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>team_id</code>, <code>user_id</code>, <code>leader</code>, <code>validated</code>, <code>created_at</code>, <code>updated_at</code>, <code>occurrence</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### teams_users / show

**GET** `/v2/teams_users/:id`

Return the team_user specified by the `:id` parameter

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### teams_users / create

**POST** `/v2/teams_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `teams_user` | No | hash | Must be a Hash |

### teams_users / update

**PATCH** `/v2/teams_users/:id`

**PUT** `/v2/teams_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `teams_user` | No | hash | Must be a Hash |

### teams_users / destroy

**DELETE** `/v2/teams_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## titles

Titles a [user](#users) can obtain, generally through achievements. It will be displayed on their profile and on the forum.

### titles / index

**GET** `/v2/titles`

**GET** `/v2/users/:user_id/titles`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### titles / show

**GET** `/v2/titles/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### titles / create

**POST** `/v2/titles`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `title` | No | hash | Must be a Hash |

### titles / update

**PATCH** `/v2/titles/:id`

**PUT** `/v2/titles/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `title` | No | hash | Must be a Hash |

### titles / destroy

**DELETE** `/v2/titles/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## titles_users

[Users](#users) who have a [title](#title).

### titles_users / index

**GET** `/v2/titles/:title_id/titles_users`

**GET** `/v2/users/:user_id/titles_users`

**GET** `/v2/titles_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `title_id` | No | string | The title id or slug (Must be String |
| `user_id` | No | string | The user id or slug (Must be String |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### titles_users / show

**GET** `/v2/titles_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### titles_users / create

**POST** `/v2/titles_users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `titles_user` | No | hash | Must be a Hash |

### titles_users / update

**PATCH** `/v2/titles_users/:id`

**PUT** `/v2/titles_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `titles_user` | No | hash | Must be a Hash |

### titles_users / destroy

**DELETE** `/v2/titles_users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## transactions

Transaction represents Altarian Dollars earned.

### transactions / index

**GET** `/v2/transactions`

**GET** `/v2/users/:user_id/transactions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>value</code>, <code>user_id</code>, <code>transactable_id</code>, <code>transactable_type</code>, <code>created_at</code>, <code>reason</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>value</code>, <code>user_id</code>, <code>transactable_id</code>, <code>transactable_type</code>, <code>created_at</code>, <code>reason</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### transactions / show

**GET** `/v2/transactions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### transactions / create

**POST** `/v2/transactions`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `transaction` | No | hash | Must be a Hash |

### transactions / update

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `transaction` | No | hash | Must be a Hash |

### transactions / destroy

**DELETE** `/v2/transactions/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## translations

Translations

### translations / index

**GET** `/v2/translations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>translatable_id</code>, <code>translatable_type</code>, <code>language_id</code>, <code>fields</code>, <code>created_at</code>, <code>updated_at</code>, <code>user_id</code>, <code>default</code>, <code>up_to_date</code>, <code>translations_structure_id</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>translatable_id</code>, <code>translatable_type</code>, <code>language_id</code>, <code>fields</code>, <code>created_at</code>, <code>updated_at</code>, <code>user_id</code>, <code>default</code>, <code>up_to_date</code>, <code>translations_structure_id</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### translations / show

**GET** `/v2/translations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### translations / create

**POST** `/v2/translations`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `translation` | No | hash | Must be a Hash |

### translations / update

**PATCH** `/v2/translations/:id`

**PUT** `/v2/translations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `translation` | No | hash | Must be a Hash |

### translations / destroy

**DELETE** `/v2/translations/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### translations / upload

**POST** `/v2/translations/upload` — Upload a file translation

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `file` | Yes | string | yml or json (Must be File |

## user_candidatures

The candidature of an [user](#users)

### user_candidatures / index

**GET** `/v2/user_candidatures`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at desc, id desc by default. (Must be one of: <code>id</code>, <code>user_id</code>, <code>birth_date</code>, <code>gender</code>, <code>zip_code</code>, <code>country</code>, <code>birth_city</code>, <code>birth_country</code>, <code>postal_street</code>, <code>postal_complement</code>, <code>postal_city</code>, <code>postal_zip_code</code>, <code>postal_country</code>, <code>contact_affiliation</code>, <code>contact_last_name</code>, <code>contact_first_name</code>, <code>contact_phone1</code>, <code>contact_phone2</code>, <code>max_level_memory</code>, <code>max_level_logic</code>, <code>other_information</code>, <code>language</code>, <code>meeting_date</code>, <code>piscine_date</code>, <code>created_at</code>, <code>updated_at</code>, <code>phone</code>, <code>email</code>, <code>pin</code>, <code>phone_country_code</code>, <code>hidden_phone</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>user_id</code>, <code>birth_date</code>, <code>gender</code>, <code>country</code>, <code>birth_country</code>, <code>postal_country</code>, <code>piscine_date</code>, <code>email</code>, <code>campus_id</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>user_id</code>, <code>birth_date</code>, <code>gender</code>, <code>country</code>, <code>birth_country</code>, <code>postal_country</code>, <code>piscine_date</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### user_candidatures / show

**GET** `/v2/users/:user_id/user_candidature`

**GET** `/v2/user_candidatures/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### user_candidatures / create

**POST** `/v2/users/:user_id/user_candidature`

**POST** `/v2/user_candidatures`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `user_candidature` | No | hash | Must be a Hash |

### user_candidatures / update

**PATCH** `/v2/users/:user_id/user_candidature`

**PUT** `/v2/users/:user_id/user_candidature`

**PATCH** `/v2/user_candidatures/:id`

**PUT** `/v2/user_candidatures/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user_id` | No | string | The user id or slug (Must be String |
| `id` | Yes | string | The requested id (Must be String |
| `user_candidature` | No | hash | Must be a Hash |

## users

A 42 student, staff, or any entity with a 42 account.

### users / graph

**GET** `/v2/users/graph(/on/:field(/by/:interval))`

Count all occurences on a particular field (default on `created_at`) by a particular period, starting from the first occurence to now.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `field` | No | string | The date field to graph on. Default to `created_at`. (Must be one of: <code>created_at</code>, <code>updated_at</code>. |
| `interval` | No | string | The interval to graph by. Default to `month_of_year`. (Must be one of: <code>day</code>, <code>week</code>, <code>month</code>, <code>quarter</code>, <code>year</code>, <code>hour_of_day</code>, <code>day_of_week</code>, <code>day_of_month</code>, <code>month_of_year</code>. |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>login</code>, <code>email</code>, <code>encrypted_password</code>, <code>reset_password_token</code>, <code>reset_password_sent_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>image</code>, <code>first_name</code>, <code>last_name</code>, <code>pool_year</code>, <code>pool_month</code>, <code>kind</code>, <code>status</code>, <code>otp_secret_key</code>, <code>otp_tmp</code>, <code>otp_activated</code>, <code>otp_backup_passwords</code>, <code>slack_team</code>, <code>slack_login</code>, <code>slack_mail</code>, <code>slack_code_validation</code>, <code>slack_validated_at</code>, <code>token_id</code>, <code>email_stop</code>, <code>linked_user_id</code>, <code>usual_first_name</code>, <code>last_seen_at</code>, <code>password_changed_at</code>, <code>encrypted_single_usage_password</code>, <code>first_warn_anon_sent_at</code>, <code>second_warn_anon_sent_at</code>, <code>alumnized_at</code>, <code>anonymized_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>login</code>, <code>email</code>, <code>created_at</code>, <code>updated_at</code>, <code>pool_year</code>, <code>pool_month</code>, <code>kind</code>, <code>status</code>, <code>primary_campus_id</code>, <code>first_name</code>, <code>last_name</code>, <code>alumni?</code>, <code>staff?</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>login</code>, <code>email</code>, <code>created_at</code>, <code>updated_at</code>, <code>pool_year</code>, <code>pool_month</code>, <code>kind</code>, <code>status</code>. |

### users / add_correction_point

**POST** `/v2/users/:id/correction_points/add` — Add an evaluation point

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The user login (Must be String |
| `reason` | Yes | string | The reason of this evaluation point addition (Must be String |
| `amount` | No | string | The amount you want to add, if not specified it will add 1 point (Must be String |

### users / remove_correction_point

**DELETE** `/v2/users/:id/correction_points/remove` — Remove a evaluation point

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The user login (Must be String |
| `reason` | Yes | string | The reason of this evaluation point removal (Must be String |
| `amount` | No | string | The amount you want to remove, if not specified it will remove 1 point (Must be String |

### users / locations_stats

**GET** `/v2/users/:id/locations_stats` — Get location stats of a [User](#user).

This route returns the total amount of hours spent by the targeted user between the `begin_at` and `end_at`.

By default, this will return the data from the last 4 months.

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `begin_at` | No | string | Must be String |
| `end_at` | No | string | Must be String |
| `time_zone` | No | string | The timezone you want to see the locations with. Defaults to the target user’s timezone. (Must be String |

### users / exam

**GET** `/v2/users/:id/exam` — Show the exam status for the requested user

**Warning:**

This route is deprecated and will be removed, tuesday 2 august 2023.

### users / index

**GET** `/v2/coalitions/:coalition_id/users`

**GET** `/v2/dashes/:dash_id/users`

**GET** `/v2/events/:event_id/users`

**GET** `/v2/accreditations/:accreditation_id/users`

**GET** `/v2/teams/:team_id/users`

**GET** `/v2/projects/:project_id/users`

**GET** `/v2/partnerships/:partnership_id/users`

**GET** `/v2/expertises/:expertise_id/users`

**GET** `/v2/users`

**GET** `/v2/cursus/:cursus_id/users`

**GET** `/v2/campus/:campus_id/users`

**GET** `/v2/achievements/:achievement_id/users`

**GET** `/v2/titles/:title_id/users`

**GET** `/v2/quests/:quest_id/users`

**GET** `/v2/groups/:group_id/users`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `coalition_id` | No | string | The coalition id or slug (Must be String |
| `dash_id` | No | string | The dash id or slug (Must be String |
| `event_id` | No | string | The event id (Must be String |
| `accreditation_id` | No | string | The accreditation id (Must be String |
| `team_id` | No | string | The team id (Must be String |
| `project_id` | No | string | The project id or slug (Must be String |
| `partnership_id` | No | string | The partnership id or slug (Must be String |
| `expertise_id` | No | string | The expertise id or slug (Must be String |
| `cursus_id` | No | string | The cursus id or slug (Must be String |
| `campus_id` | No | string | The campus id or slug (Must be String |
| `achievement_id` | No | string | The achievement id or slug (Must be String |
| `title_id` | No | string | The title id or slug (Must be String |
| `quest_id` | No | string | The quest id or slug (Must be String |
| `group_id` | No | string | The group id (Must be String |
| `sort` | No | string | The sort field. Sorted by id desc by default. (Must be one of: <code>id</code>, <code>login</code>, <code>email</code>, <code>encrypted_password</code>, <code>reset_password_token</code>, <code>reset_password_sent_at</code>, <code>created_at</code>, <code>updated_at</code>, <code>image</code>, <code>first_name</code>, <code>last_name</code>, <code>pool_year</code>, <code>pool_month</code>, <code>kind</code>, <code>status</code>, <code>otp_secret_key</code>, <code>otp_tmp</code>, <code>otp_activated</code>, <code>otp_backup_passwords</code>, <code>slack_team</code>, <code>slack_login</code>, <code>slack_mail</code>, <code>slack_code_validation</code>, <code>slack_validated_at</code>, <code>token_id</code>, <code>email_stop</code>, <code>linked_user_id</code>, <code>usual_first_name</code>, <code>last_seen_at</code>, <code>password_changed_at</code>, <code>encrypted_single_usage_password</code>, <code>first_warn_anon_sent_at</code>, <code>second_warn_anon_sent_at</code>, <code>alumnized_at</code>, <code>anonymized_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>login</code>, <code>email</code>, <code>created_at</code>, <code>updated_at</code>, <code>pool_year</code>, <code>pool_month</code>, <code>kind</code>, <code>status</code>, <code>primary_campus_id</code>, <code>first_name</code>, <code>last_name</code>, <code>alumni?</code>, <code>staff?</code>. |
| `range` | No | string | Select on a particular range (Must be one of: <code>id</code>, <code>login</code>, <code>email</code>, <code>created_at</code>, <code>updated_at</code>, <code>pool_year</code>, <code>pool_month</code>, <code>kind</code>, <code>status</code>. |

### users / show

**GET** `/v2/users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

### users / create

**POST** `/v2/users`

**This is the main call for user creation on the 42 ecosystem.**

This call requires at least the `email`, `campus_id`, `first_name` and `last_name` fields. If the login isn’t specified, it will be generated from the supplied `first_name` and the `last_name`. **If no cursus is supplied, the user will join the cursus `piscine-c` by default**.

If an endpoint is configured for the supplied campus, it will be triggered before save. You can read more about campus endpoints on [the endpoint documentation](/apidoc/2.0/endpoint.html).

This call also accept additional data, nested under `user_candidature_attributes`, wich can be added later with the [user candidature call](/apidoc/2.0/user_candidature/create.html) and is only visible for the user and at least the `basic_staff` role. The supplied email must be the personal email of the user. It will be moved to user_candidature after save, replacer by the given campus’s alias. Adding an image will generate an original, a medium and a small version of this one.

The `meta` key allow a hash with `ldap_group`. The `ldap_group` has transmited to LDAP server if campus is

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `user` | No | hash | Must be a Hash |

### users / update

**PATCH** `/v2/users/:id`

**PUT** `/v2/users/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
| `user` | No | hash | Must be a Hash |

### users / me

**GET** `/v2/me` — Show the current resource owner

Will respond with the current resource owner, wich is the token owner (the actually logged-in user).

### users / free_past_agu

**POST** `/v2/users/:id/free_past_agu` — free past agu to user

Add a free agu in the past for a user which implies to delay the blackhole, Please follow the rules about the free agu. (if you dont know the rules contact a 42network staff)

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The user login (Must be String |
| `duration` | Yes | string | Blackhole delay duration in day (Must be String |
| `reason` | No | string | Optional reason for the freeze. (Must be String |

### users / unfreeze

**POST** `/v2/users/:user_id/unfreeze` — Unfreeze user

End all agus

### users / set_primary_campus

**POST** `/v2/users/:id/set_primary_campus` — Set primary campus

Set the primary campus for the user

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `campus_id` | Yes | numeric | The campus id (Must be Integer |

### users / alumnize

**POST** `/v2/users/:id/alumnize` — Alumnize user

Alumnize user

### users / dealumnize

**POST** `/v2/users/:id/dealumnize`

Dealumnize user

### users / deactivate_2fa

**DELETE** `/v2/users/:id/otp_settings/remove` — Deactivate 2FA

Deactivate student 2FA

### users / staff

**GET** `/v2/staff` — Get all staff

Get all staff

### users / allowed_registration_projects

**GET** `/v2/users/:user_id/projects_users/registration` — Get all allowed registration projects for a user

This route returns all the projects for which the user can register.

## waitlists

Waitlist for an [event](#events) or an [exam](#exams).

### waitlists / index

**GET** `/v2/waitlists`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `sort` | No | string | The sort field. Sorted by created_at asc, id desc by default. (Must be one of: <code>id</code>, <code>waitlistable_id</code>, <code>waitlistable_type</code>, <code>created_at</code>, <code>updated_at</code>. |
| `filter` | No | string | Filtering on one or more fields (Must be one of: <code>id</code>, <code>waitlistable_id</code>, <code>waitlistable_type</code>, <code>created_at</code>, <code>updated_at</code>. |
| `page` | No | hash | The pagination params, as a hash (Must be a Hash |

### waitlists / show

**GET** `/v2/events/:event_id/waitlist`

**GET** `/v2/exams/:exam_id/waitlist`

**GET** `/v2/waitlists/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `event_id` | No | string | The event id (Must be String |
| `exam_id` | No | string | The exam id (Must be String |
| `id` | Yes | string | The requested id (Must be String |

### waitlists / destroy

**DELETE** `/v2/waitlists/:id`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |

## webhook_registeries

Webhook Registeries

### webhook_registeries / deactivate

**POST** `/v2/webhook_registeries/:id/deactivate`

**Parameters:**

| Name | Required | Type | Description |
|------|----------|------|-------------|
| `id` | Yes | string | The requested id (Must be String |
