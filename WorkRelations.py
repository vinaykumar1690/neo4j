
# Return a node's work relations
# Return None if none exists
#
def get_work_rels(node):
	rels = node.get_properties()

	if "workExperienceRelationshipIdList" in rels:
		rels = node.get_properties()["workExperienceRelationshipIdList"]		
		return rels
	else:
		return None


# Return a node's workplace as a list of nodes
# Return None if none
#
def works_at(node, graph_db):

	works_at = []

	node_rels = get_work_rels(node)

	if node_rels == None:
		return None
	else:
		for relation_id in node_rels:
			work_relation = graph_db.relationship(relation_id)
			node_works_at = work_relation.end_node

			works_at.append(node_works_at)

		return works_at


# Return True if two nodes have worked at the same place
# False otherwise
def work_relation(start_node, end_node, graph_db):

	start_node_workplaces = works_at(start_node, graph_db)
	end_node_workplaces = works_at(end_node, graph_db)

	if (start_node_workplaces == None or end_node_workplaces == None):
		return False
	else:
		if list(set(start_node_workplaces).intersection(end_node_workplaces)):
			return True
		else:
			return False
	