
**local notice:**
UI: http://localhost:4200/
api: 
- only one /api/
- use 8080 
- url http://localhost:8080/api/testScheduler?frequency=weekly&isDryRun=true
apikey: check application.properties 

**other env**:
api: 
- two /api/
- dont use 8080 as url
- url https://dev.regulatoryregistry.gov.on.ca/api/api/testScheduler?frequency=weekly&isDryRun=true

**bitbucket:**
Username: andy.liu2@ontario.ca
Temp Password: Friday2025$

**RR public secure:**
Username: andy.liu2@ontario.ca
Temp Password: L1uConG0813!

andydiii0813@gmail.com
L1uConG0813!

c644liu@uwaterloo.ca
l1uConG0813!

**Legacy RR backoffice UAT:**
https://intra.stage.sus.gov.on.ca/registryadmin/bo_login.jsp

Admin:
User ID: chenji
Password: ORRM_test123!

Editor:
User ID: chen1ji
Password: ORRM_test123!

**back end:**
- PostingController is for the api of posting
- PostingDTO is the data from DB after converting the type e.g. Date-> format tobe 'd mm y'
- Posting is the raw data from DB without any converting the type

controller(request) 
-> service 
-> repository 
-> entity <-> DB

**email alert trigger in postman:**
URL: https://dev.regulatoryregistry.gov.on.ca/api/api/testScheduler?frequency=daily&isDryRun=true

replace the domain to the current domain

misccontroller testscheduler params in postman

in postman specify post method, params will be auto changed once url is put in, header need to add X-API-KEY, value depends on differnt env, we can find it in search application will give something like `application.dev.property`. (application.property is local env file)

url: https://dev.regulatoryregistry.gov.on.ca/api/api/testScheduler?frequency=daily&isDryRun=true

isdryrun set to true means wont trigger real eamail sent rn, but false will trigger it to be sent right now.

this test is based on today morning's expected email alert to be received.

weekly:
postings that updated *last 7 days* suppose today is tuesday, if there is update from last tuesday to this monday then we get alert. different than normal we receive weekly on monday for the updates between last monday to sunday.


## RR testing sender email
orrm.test@gmail.com
ORRM_test!2025 

orrm.test2@gmail.com
ORRM_test!2025 

## git pull
git pull origin main - merge from remote main into local andy-dev, but this uses default merge(cause the original commit messages combined into one merge commit message), not fast-forward merge( will have same commit messages as original ones).

what people do:
1. pull remote dev into local dev first.
2. **fast-forward** merge local dev into local andy-dev. (local andy-dev will show exactly same commits as locla-dev & remote-dev)
3. commit and push local new changes to remote andy-dev. (this will take commits from remote dev(as we merged local-dev into local-andy) and new changes made myself onto remote andy-dev). 

controller 对应api url，比如api/positng/specification 就在controller posting controller.

https://localhost:8080/api is the request for backend 
https://localhost:4200 is for frontend


domain(after the https://) <-> Ip address followed by an port number like 8080, 4200...
localhost <-> 127.0.1 is the local IP address 
localhost is a variable for IP address


## eSMT
incident are the defects found in PROD.
CR wont issue a ticket but just in SP.


## self testing local for 280
1. update profile, everything except title unchanged - DONE
2. update profile, subtitle wrong when user is organization user - Fixed
3. update profile, leave title blank, everthing else fileld out, error expected - DONE 
4. create a new organization user profile  - DONE
5. create a new organization guest profile - DONE
