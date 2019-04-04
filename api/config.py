
patterns = {'AADHAR':'\d{4} \d{4} \d{4}',
			'PAN':'[A-Za-z]{5}\d{4}[A-Za-z]{1}',
			'DRIVING_LICENCE':'[A-Za-z]{2}\d{14}',
			'PASSPORT':'J\d{7}'
			}

id_list = {'AADHAR':[1,'Name','DOB','ID'],
		   'PAN':[2,'Name','FName','DOB','ID'],
		   'DRIVING_LICENCE':[3,'Name','FName','Issued On','ID'],
		   'PASSPORT':[0,'Name','DOB','ID']
		   }
