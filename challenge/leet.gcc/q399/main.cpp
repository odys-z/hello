/**
 * 399. Evaluate Division
 * https://leetcode.com/problems/evaluate-division/
 *
 */
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <assert.h>

using namespace std;

class Variable {
public:
    map<string, double> mulwith;
    string name;
    double val; // my value for returned as sub graph's evaluated
    bool visited;

    /**For declaring before finding when initializing
     * https://stackoverflow.com/a/13570219/7362888
     * @brief Variable
     */
    Variable() : name(""), val(1.0), visited(false) {}

    Variable(string name) : name(name), val(1.0), visited(false)
    { }

    void addEdge(string n, double v)
    {
        if (n != name)
            mulwith.insert(pair<string, double>(n, v));
    }
};

/**
 * 100.00% 0ms, 55.39% 4ms
 *
 * @brief The Sol100Percent class
 */
class Sol100Percent {
    double evaluate(map<string, Variable> &nodes, vector<string> &expr)
    {
        map<string, bool> visited;
        queue<Variable*> rim;

        map<string, Variable>::iterator root = nodes.find(expr[0]);
        if (root == nodes.end() or nodes.find(expr[1]) == nodes.end())
            return -1;
        else if (expr[1] == expr[0])
            return 1;

        root->second.val = 1.0;
        rim.push(&root->second);

        return bfs(rim, expr[1], nodes);
    }

    double bfs(queue<Variable*> q, string until, map<string, Variable> &nodes)
    {
        queue<Variable*> rim;
        while (q.size() > 0)
        {
            Variable *me = q.front(); q.pop();
            me->visited = true;

            for (const auto &mulwith: me->mulwith)
            {
                map<string, Variable>::iterator var = nodes.find(mulwith.first);

                if (var == nodes.end())
                    return -1;

                if (var->second.name == until)
                    return me->val * mulwith.second;
                if (!var->second.visited)
                {
                    var->second.val = me->val * mulwith.second;
                    rim.push(&var->second);
                }
            }
        }

        if (rim.size() == 0)
            return -1;
        else
            return bfs(rim, until, nodes);
    }

public:
    vector<double> calcEquation(vector<vector<string>>& eqs, vector<double>& vals, vector<vector<string>>& queries) {
        map<string, Variable> nodes;

        for (ulong x = 0; x < eqs.size(); x++)
        {
            if (eqs[x][0] == eqs[x][1]) continue;

            Variable *n, *d;
            map<string, Variable>::iterator itn = nodes.find(eqs[x][0]);
            map<string, Variable>::iterator itd = nodes.find(eqs[x][1]);
            if (itn != nodes.end())
                n = &itn->second;
            else n = new Variable(eqs[x][0]);
            if (itd != nodes.end())
                d = &itd->second;
            else d = new Variable(eqs[x][1]);

            n->addEdge(eqs[x][1], vals[x]);
            d->addEdge(eqs[x][0], 1.0 / vals[x]);

            nodes.insert(pair<string, Variable>(n->name, *n));
            nodes.insert(pair<string, Variable>(d->name, *d));
        }

        vector<double> rest;
        for (vector<string> q : queries)
        {
            map<string, Variable>::iterator it = nodes.begin();
            while (it != nodes.end())
            {
                it->second.visited = false;
                it++;
            }
            rest.push_back(evaluate(nodes, q));
        }

        return rest;
    }
};

/**
 * 100.00%, 0ms
 * @brief BFS with node structure, without rescursion
 */
class Solution
{
public:
    vector<double> calcEquation(vector<vector<string>>& eqs, vector<double>& vals, vector<vector<string>>& queries) {
        map<string, Variable> nodes;

        for (ulong x = 0; x < eqs.size(); x++)
        {
            if (eqs[x][0] == eqs[x][1]) continue;

            Variable *n, *d;
            map<string, Variable>::iterator itn = nodes.find(eqs[x][0]);
            map<string, Variable>::iterator itd = nodes.find(eqs[x][1]);
            if (itn != nodes.end())
                n = &itn->second;
            else n = new Variable(eqs[x][0]);
            if (itd != nodes.end())
                d = &itd->second;
            else d = new Variable(eqs[x][1]);

            n->addEdge(eqs[x][1], vals[x]);
            d->addEdge(eqs[x][0], 1.0 / vals[x]);

            nodes.insert(pair<string, Variable>(n->name, *n));
            nodes.insert(pair<string, Variable>(d->name, *d));
        }

        vector<double> rest;
        for (vector<string> q : queries)
        {

            rest.push_back(evaluate(nodes, q[0], q[1]));
        }

        return rest;
    }

    double evaluate(map<string, Variable> & nodes, string n0, string d9)
    {
        if (nodes.find(n0) == nodes.end() or nodes.find(d9) == nodes.end())
            return -1;
        else if (n0 == d9) return 1;

        set<string> visited;
        queue<string> q;
        // root's value not always 1 - updated by last round.
        double v0 = nodes.find(n0)->second.val;
        q.push(n0);

        while (q.size() > 0)
        {
            queue<string> q_;
            while(q.size() > 0)
            {
                Variable *me = &nodes.find(q.front())->second; q.pop();
                visited.insert(me->name);
                if (me->name == d9)
                    return me->val;

                for (const auto &edge : me->mulwith)
                {
                    map<string, Variable>::iterator toIt = nodes.find(edge.first);
                    if (toIt == nodes.end()) return -1;

                    Variable* to = &toIt->second;
                    if (to->name == d9)
                        return me->val * edge.second / v0;
                    if (visited.find(to->name) == visited.end())
                    {
                        to->val = me->val * edge.second;
                        q_.push(to->name);
                    }
                }
            }
            q = q_;
        }
        return -1;
    }
};

/**
 * 8.07% 9ms
 * @brief The Solution class
 */
class SolutionArrayBuf {
    map<string, int> names;
    vector<bool> visited;

    /** [nominator, denominator] */
    vector<vector<double>> edges;

    int maxv;
public:
    vector<double> calcEquation(vector<vector<string>>& eqs, vector<double>& vals, vector<vector<string>>& queries) {
        names.clear();
        maxv = eqs.size() * 2;
        vector<vector<double>> edges(maxv, vector<double>(maxv, 0));

        for (ulong x = 0; x < eqs.size(); x++)
        {
            vector<string> eq = eqs[x];
            string n = eq[0], d = eq[1];
            int nId = -1, dId = -1;
            if (names.find(n) == names.end())
            {
                nId = names.size();
                names.insert(pair<string, int>(n, nId));
            }
            else nId = names[n];
            if (names.find(d) == names.end())
            {
                dId = names.size();
                names.insert(pair<string, int>(d, dId));
            }
            else dId = names[d];
            if (nId >= 0 and dId >=0)
            {
                edges[nId][dId] = vals[x];
                edges[dId][nId] = 1. / vals[x];
            }
            else if (nId == dId)
                edges[nId][dId] = 1.;
        }
        maxv = names.size();
        this->edges = edges;

        vector<bool> visited(maxv, false);
        this->visited = visited;

        vector<double> reslts;
        for (vector<string> qry : queries)
        {
            for (int i = 0; i < maxv; i++)
            {
                this->edges[i][i] = 1.;
                this->visited[i] = false;
            }

            queue<int> root;
            if (names.find(qry[0]) != names.end() and names.find(qry[1]) != names.end())
            {
                root.push(names[qry[0]]);
                reslts.push_back(bfs(root, names[qry[1]]));
            }
            else
                reslts.push_back(-1);
        }
        return reslts;
    }

    double bfs(queue<int> rim, int until)
    {
        queue<int> q;
        while(rim.size() > 0)
        {
            int me = rim.front(); rim.pop();
            visited[me] = true;
            if (me == until)
                return edges[me][me];

            for (int dx = 0; dx < maxv; dx++)
            {
                if (dx == until and edges[me][dx] != 0)
                    return edges[me][me] * edges[me][dx];
                if (dx == me) continue;
                if (!visited[dx] and edges[me][dx] != 0)
                {
                    q.push(dx);
                    edges[dx][dx] = edges[me][me] * edges[me][dx];
                }
            }
        }

        if (q.size() > 0)
            return bfs(q, until);
        else
            return -1.;
    }
};

int main()
{
    // SolutionArrayBuf s1;
    Solution s1;
    Sol100Percent s;

    vector<vector<string>> eqs = {{"a", "b"}, {"b", "c"}};
    vector<double> vals = {2.0, 1.25};
    vector<vector<string>> qries = {{"a", "c"}, {"c", "b"}};
    vector<double> answers = s.calcEquation(eqs, vals, qries);
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    vector<double> ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    eqs = {{"a","b"},{"c","d"}};
    vals = {1.0,1.0};
    qries = {{"a","c"},{"b","d"},{"b","a"},{"d","c"}};
    cout << " output: 1., -1, 1, 1" << endl;
    answers = s.calcEquation(eqs, vals, qries);
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    eqs = {{"x1","x2"},{"x2","x3"},{"x3","x4"},{"x4","x5"}} ;
    vals = {3.0,4.0,5.0,6.0};
    qries = {{"x1","x5"},{"x5","x2"},{"x2","x4"},{"x2","x2"},{"x2","x9"},{"x9","x9"}};
    cout << " output: 360., ..." << endl;
    answers = s.calcEquation(eqs, vals, qries);
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    eqs = {{"a","e"}, {"b","e"}};
    vals = {4, 3};
    qries = {{"a","b"},{"e","e"},{"x","x"}};
    cout << " output: 4/3, 1, -1" << endl;
    answers = s.calcEquation(eqs, vals, qries);
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    eqs = {{"a", "b"}, {"b", "c"}};
    vals = {2.0, 3.};
    qries = {{"a", "c"}, {"b", "a"}, {"a","e"}, {"a","a"}, {"x","x"}};
    answers = s.calcEquation(eqs, vals, qries);
    cout << "[6.0, 0.50, -1.0, 1.0, -1.0]" << endl;
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    eqs = {{"a","b"}, {"b","c"}, {"bc","cd"}};
    vals = {1.5,2.5,5.0};
    qries = {{"a","c"}, {"c","b"}, {"bc","cd"}, {"cd","bc"}};
    cout << "Output: [3.750, 0.4, 5.0, 0.2]" << endl;
    answers = s.calcEquation(eqs, vals, qries);
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    eqs = {{"a","b"},{"b","c"},{"bc","cd"}};
    vals = {1.5,2.5,5.0};
    qries = {{"a","c"},{"c","b"},{"bc","cd"},{"cd","bc"}};
    cout << "Output: {3.75, 0.4, 5.0, 0.2}" << endl;
    answers = s.calcEquation(eqs, vals, qries);
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    eqs = {{"a","b"}};
    vals = {0.5};
    qries = {{"a","b"},{"b","a"},{"a","c"},{"x","y"}};
    cout << "Output: {0.50,2.,-1.,-1.}" << endl;
    answers = s.calcEquation(eqs, vals, qries);
    for (double ans : answers)
        cout << ans << " ";
    cout << endl;
    ans1 = s1.calcEquation(eqs, vals, qries);
    for (ulong x = 0; x < answers.size(); x++)
        assert(answers[x] == ans1[x]);

    /*
     * [["a","b"],["b","c"],["c", "d"],["d","e"], ["e", "f"], ["d", "g"], ["g", "h"]]
     * [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
     * [["a","f"],["d","h"]]
     *
     * [32.00000,4.00000]
     */
    cout << "OK!" << endl;
    return 0;
}
