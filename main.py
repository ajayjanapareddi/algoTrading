app_id = "HENZC71F50-100"
secret_id ="CBEW6TZP74"
redirect_url="https://in.tradingview.com/chart/a3xqgpVc/?symbol=BSE%3ASENSEX"


from fyers_api import accessToken

# convert it to api and either have redis or sql to store auth code.
# add a scheduler or when ever auth code is expired we need to have scheduler or something so that it automatically upades the redis. 
# def getAccessToken():
session=accessToken.SessionModel(
client_id=app_id,
secret_key=secret_id,
redirect_uri=redirect_url, 
response_type="code",
grant_type ="authorization_code"
)
response = session.generate_authcode()
print (response)
auth_code = input("please enter auth code")
session.set_token(auth_code)
accessToken= session.generate_token()["access_token"]
