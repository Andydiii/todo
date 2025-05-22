## LRO uploading file to SP steps:
termiology: 
1. Microsoft Entra ID(same as Microsoft AD) used for app IAM, registration/authentication... so client can use microsoft api and so on in the app...
2. PnP powershell is a module that provides cmdlets(reads as command-lets), and cmdlets is the command in the windows powershell command line environment.
3. certification (Microsoft Entra ID certificate-based authentication (CBA) allows organizations to authenticate users using X.509 certificates.)
4. JWT(Json web token) = client assertion, used to get a Bearer access token

## Steps
**Set up in Azure Entra ID:**
1. register the app in Azure Entra ID
2. Create X.509 certificate with PnP PowerShell and `New-PnPAzureCertificate` cmdlet
   1. generate two files, one ends with `pfx` and one ends with `cer`
   2. Go back to the Entra ID application and click `Certificate & secrete` and select `Certification` upload the `.CER `file to certification
3. add api permission for `sites.selected`. it cannot be used until a global admin grants the admin consent. this needs to submit a ticket to IT to grant. 
**Set up in Application**
4. Grant my app read and write permission to specific sharepoint site using PnP powershell and followting comlets:
   1. `Connect-PnPOnline` -Interactive -Url "https://contoso.sharepoint.com/sites/projects" -clientId d37c6218-bef5-49f1-89ef-0b02814f785e
   2. `Grant-PnPAzureADAppSitePermission` -AppId "<App ID in Entra ID>" -DisplayName "My Test App" -Permissions FullControl -Site https://contoso.sharepoint.com/sites/projects
5. set up configuration file that contains tenantID ClientID & `.CER` file path in the machine and certificate password.
6. creates a JWT(Json Web token)/client assertion with the certificate, then sends the JWT to Azure AD to get an Bearer access token(the access token is used to authenticate).
7. use the Bearer access token in the authorization header to call sharepoint's REST API to uploads files