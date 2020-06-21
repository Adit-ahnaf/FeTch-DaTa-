from rest_framework import serializers
from Apiapp.models  import Data 

class DataSerealizer(serializers.ModelSerializer):

	class Meta:
		model = Data
		fields = '__all__'