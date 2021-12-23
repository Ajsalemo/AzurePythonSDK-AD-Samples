# python-flask-msal-quickstart

This sample is taken from [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-python-webapp). This sample has been slimmed down from the one in link to focus on simple authentication usage.

### Getting started
 - You can use the above link to create a new Azure AD application or [register](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/applicationsListBlade/quickStartType/PythonQuickstartPage/sourceType/docs) a new one

#### Using an existing Azure AD application
 - If using an existing Azure AD application you'll need the following credentials
   - Client (Application) ID
   - Client Secret
 - You'll need to configure a Redirect UI as well.
   - Go to your Azure AD Application -> Authentication <br>
    ![image](https://user-images.githubusercontent.com/31021304/147167636-7581372e-fa68-4447-bbce-ed4defcad18f.png)
   - If needed, select 'Add a platform' -> select 'Web' <br>
    ![image](https://user-images.githubusercontent.com/31021304/147167675-b1bfb10b-805c-4d11-b2dd-bfbfe726bd92.png) <br>
    ![image](https://user-images.githubusercontent.com/31021304/147167742-e107c14c-8414-4856-b813-6cfbd0ab852f.png)
   - Set your Redirect UI to `http://localhost:5000/callback`, or your path of choosing. <br>
    ![image](https://user-images.githubusercontent.com/31021304/147167843-81eeb860-3ac2-47e0-a48e-e641d26cfcfd.png)
#### Permissions
- Go to the Azure Active Directory application that was created
- Choose `API permissions` on the left sidenav <br>
  ![image](https://user-images.githubusercontent.com/31021304/147167908-39e6f82b-f78b-4985-93a1-38eb6b92ee23.png)
- Select the `User.Read` and `User.ReadBasic.All` permissions from Microsoft Graph. Click 'Add permissions' to save.
  ![image](https://user-images.githubusercontent.com/31021304/147167945-f742765d-fba5-409c-b840-38b1daed0e39.png)
  
#### Running the sample
- Make sure to replace the environment variables `CLIENT_SECRET`, `CLIENT_ID` and `REDIRECT_PATH` with the values taken above from Client ID, Client Secret and your Redirect UI in `app_config.py` using an .env file.
- Create and activate your virtual environment and run `pip install -r requirements.txt`.
- Run `flask run`.
