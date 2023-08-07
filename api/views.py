from rest_framework.response import Response
from rest_framework.decorators import api_view
from us_list.models import User
from .serializers import UserSerializer

def matches_criteria(value, criteria):
    """Checks if the given value matches the criteria."""
    if criteria is None or value is None:  # Ensure neither is None before proceeding
        return False
    
    value_str = str(value)
    criteria_str = str(criteria)
    
    if(value_str == criteria_str or criteria_str.find(value_str) != -1):
          return True
      
    # check matching at least length - 1 letters.  
    matchNum = 0
    lastIndex = -1
    
    value_array = [char for char in value_str]
    criteria_array = [char for char in criteria_str]
       
    for valueChar in value_array:

        for indexCriteria,criteriaChar in enumerate(criteria_array):
            if(valueChar == criteriaChar and (indexCriteria > lastIndex  or lastIndex == -1)):
                matchNum +=1
                lastIndex = indexCriteria
                print(criteriaChar)
                break
        
        if(len(value_array) == matchNum):
            print('Yes')
            break        
    
    
    if((len(value_array) - matchNum) < 2 and matchNum != 0):
        print(value_array)
        print(len(value_array))
        print(matchNum)
        return True
            
    return False
    
    


properties_to_check = ['category', 'nationality', 'family_arabic','family_english','fullname_arabic',
                       'fullname_english','birth_date','birth_place','nick_name','street','city',
                       'country','type','document_number','issuer','from_date','to_date']  # add other properties here


@api_view(['POST'])
def getData(request):
    print('test' , request.data['category'])
    users = User.objects.all()
    checkedUsers =[]    
    for x in users:
        # if any(matches_criteria(getattr(x, prop), request.data.get(prop)) for prop in properties_to_check):
        #         checkedUsers.append(x)
        if any(matches_criteria(getattr(x, prop), request.data.get(prop)) for prop in properties_to_check):
                checkedUsers.append(x)
    #    if(x.category == request.data['category'] or request.data['category'].find(x.category) > 0):
    #       checkedUsers.append(x)
    
    #    print(x.category.str.contains(pat = 'is'))    
    #    print(request.data['category'].find(x.category))
    #    print(x.fullname_arabic.split())
        
    serializer = UserSerializer(checkedUsers, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)