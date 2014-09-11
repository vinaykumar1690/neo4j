
# Return an institution's educationType
# Return 1 if high school or school
# Return 2 if college or graduate school or university
#
def get_education_type(educationType):

	education_type = 0

	if educationType == "High School" or educationType == "School":
		education_type = 1
	elif educationType == "College" or educationType == "Graduate School" or educationType == "University":
		education_type = 2

	return education_type

# Return a node's education relations
# Return None if none exists
#
def get_education_rels(node):
	rels = node.get_properties()

	if "educationRelationshipIdList" in rels:
		rels = node.get_properties()["educationRelationshipIdList"]

		return rels

	else:
		return None


# Return the list of schools this person attended
# Return None if none
#
def studied_at(node, graph_db):

	studied_at = []	

	node_rels = get_education_rels(node)

	if node_rels == None:
		return None
	else:
		for relation_id in node_rels:
			
			education_relation = graph_db.relationship(relation_id)

			if "educationType" in education_relation.get_properties():
				education_type = get_education_type(education_relation.get_properties()["educationType"])
				node_studied_at = education_relation.end_node

				# Add education type to the properties of the end node			
				node_studied_at.update_properties({ "educationType": education_type })

				studied_at.append(node_studied_at)
				
		return studied_at


# Return 1 if two nodes have gone to the same high school/school, 
# Return 2 if they have gone to the same college/graduate school
# Return 3 if they have gone to the same high school AND college
# 0 otherwise if None
#
def education_relation(start_node, end_node, graph_db):

	start_node_schools = studied_at(start_node, graph_db)
	end_node_schools = studied_at(end_node, graph_db)
	education_relation = 0
	
	if (start_node_schools == None or end_node_schools == None):
		return 0
	else:
		common_nodes = list(set(start_node_schools).intersection(end_node_schools))
		
		if len(common_nodes) == 0:
			return 0
		else:
			common_education_types = [] # common_education_types = [1, 2] => both high school and college in common

			# Two people might have more than 1 common school
			for common_node in common_nodes:
				common_education_types.append(common_node.get_properties()["educationType"]) 

			# If we have 1 in the common_education_types
			if 1 in common_education_types and 2 in common_education_types:
				return 3
			elif 1 in common_education_types:
				return 1
			elif 2 in common_education_types:
				return 2
			else:
				return 0

	