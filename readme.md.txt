# Requirements

  * Python 3.10

> This code was developed as the showcase of basic python development.

> 
# Installation
Install the dependencies from the requirements.txt file and then you can run this script. 

# Sample Execution & Output

Run the program from its root directory with:

```
uvicorn main:vip_api --reload
```

Example request:
```
curl -X GET localhost:8000/v1/now/
```

