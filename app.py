from SINGLEPAGEAPPHW2 IMPORT SINGLEPAGEAPPHW2
import requests
SINGLEPAGEAPPHW2 = Flask(__name__)


@app.route('/')
def Hello_world():
    return "hello gorgeous! Welcome to Flask"

@app.route('/user/<name>')
def user(name):
    return f'hello{name}'


@app.route('/login', method=['GET', 'POST'])
def login():
    if request.methoed == 'POST'
    email = request.form.get('password')
    return f'{email} {password}'
else:
     return render_template('login.html')


def getDriverInfo(driver):
    driver_info ={
        'first_name': driver['Driver']['givenName'],
        'last_name': driver['Driver']['familyName'],
        'DOB': driver['Driver']['dateOfBirth'],
        'wins': driver['wins'],
        'team': driver['Constructors'][0]['name']}
    
    return driver_info

print(getDriverInfo(driver_standings[2]))

def driver_info_year_rnd(year, rnd):
    url = f'https://ergast.com/api/f1/{year}/{rnd}/driverStandings.json'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        driver_standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        for driver in driver_standings:
            driver_dict = getDriverInfo(driver)
            print(f"{driver_dict['first_name']} {driver_dict['last_name']} {driver_dict['DOB']} {driver_dict['wins']} {driver_dict['team']} \n")
    
    
@app.route('ergast', method=['GET', 'POST'])
def ergast():
    if requests.method =='POST':
        return 'something'
    else:
        return render_template('ergast.html')