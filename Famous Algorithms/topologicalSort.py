"""
Topological Sort

You're given a list of arbitrary jobs that need to be completed; these jobs are represented by distinct integers.
You're also given a list of dependencies. A dependency is represented as a pair of jobs where the first job is a
prerequisite of the second one. In other words, the second job depends on the first one;
it can only be completed once the first job is completed.

Write a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid order
in which the given jobs can be completed. If no such order exists, the function should return an empty array.

Sample Input: [1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
Sample Output: [1, 4, 3, 2] or [4, 1, 3, 2]
"""


# SOLUTION 1

# O(j + d) time | O(j + d) space
def topologicalSort1(jobs, deps):
    jobGraph = createJobGraph1(jobs, deps)
    return getOrderedJobs1(jobGraph)


def createJobGraph1(jobs, deps):
    graph = JobGraph1(jobs)
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph


def getOrderedJobs1(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse1(node, orderedJobs)
        if containsCycle:
            return []
    return orderedJobs


def depthFirstTraverse1(node, orderedJobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = depthFirstTraverse1(prereqNode, orderedJobs)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    orderedJobs.append(node.job)
    return False


class JobGraph1:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def addNode(self, job):
        self.graph[job] = JobNode1(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]


class JobNode1:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False


# SOLUTION 2

# O(j + d) time | O(j + d) space
def topologicalSort2(jobs, deps):
    jobGraph = createJobGraph2(jobs, deps)
    return getOrderedJobs2(jobGraph)


def createJobGraph2(jobs, deps):
    graph = JobGraph2(jobs)
    for job, dep in deps:
        graph.addDep(job, dep)
    return graph


def getOrderedJobs2(graph):
    orderedJobs = []
    nodesWithNoPrereqs = list(filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
    while len(nodesWithNoPrereqs):
        node = nodesWithNoPrereqs.pop()
        orderedJobs.append(node.job)
        removeDeps2(node, nodesWithNoPrereqs)
    graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
    return [] if graphHasEdges else orderedJobs


def removeDeps2(node, nodesWithNoPrereqs):
    while len(node.deps):
        dep = node.deps.pop()
        dep.numOfPrereqs -= 1
        if dep.numOfPrereqs == 0:
            nodesWithNoPrereqs.append(dep)


class JobGraph2:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addDep(self, job, dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.deps.append(depNode)
        depNode.numOfPrereqs += 1

    def addNode(self, job):
        self.graph[job] = JobNode2(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]


class JobNode2:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.numOfPrereqs = 0
