
import WorkRelations
import EducationRelations

# Given two nodes, and the graph, return their relationship type
#
# Connected										= Type 1
# Connected + high school 						= Type 2
# Connected + college 							= Type 3
# Connected + coworker 							= Type 4
# Connected + coworker + high school 			= Type 5
# Connected + coworker + college 				= Type 6
# Connected + high school + college 			= Type 7
# Connected + high school + college + coworker	= Type 8
#
def get_relation(start_node, end_node, graph_db):

	relation_type = 1 # Connected

	# True or False
	work_relation = WorkRelations.work_relation(start_node, end_node, graph_db) 

	# 1, 2, 3 or 0
	education_relation = EducationRelations.education_relation(start_node, end_node, graph_db)

	# Dictionary of relationship types
	relationships_coworker = { 0: 4, 1: 5, 2: 6, 3: 8 }
	relationships_non_coworker = { 0: 1, 1: 2, 2: 3, 3: 7 }

	if work_relation:
		relation_type = relationships_coworker[education_relation]
	else:
		relation_type = relationships_non_coworker[education_relation]

	return relation_type
