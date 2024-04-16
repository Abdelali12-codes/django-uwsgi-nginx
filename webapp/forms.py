from django import forms

#time = "2023-06-24T17:20:40.421Z"

# time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
#print(datetime.strftime(time, '%Y/%B/%d:%d'))
# timestamp = datetime.fromisoformat(time[:-1]).replace(microsecond=0).timestamp()
# print(datetime.fromtimestamp(timestamp))

class NameForm(forms.Form):
    firstname = forms.CharField(label="firstname", required=True, max_length=20)
    lastname = forms.CharField(label="lastname", required=True, max_length=20)