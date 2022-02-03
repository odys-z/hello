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

class Variable100 {
public:
    map<string, double> mulwith;
    string name;
    double val; // my value for returned as sub graph's evaluated
    bool visited;

    /**For declaring before finding when initializing
     * https://stackoverflow.com/a/13570219/7362888
     * @brief Variable
     */
    Variable100() : name(""), val(1.0), visited(false) {}

    Variable100(string name) : name(name), val(1.0), visited(false)
    { }

    void addEdge(string n, double v)
    {
        if (n != name)
            mulwith.insert(pair<string, double>(n, v));
    }
};

class Sol100Percent {
    double evaluate(map<string, Variable100> &nodes, vector<string> &expr)
    {
        map<string, bool> visited;
        queue<Variable100*> rim;

        map<string, Variable100>::iterator root = nodes.find(expr[0]);
        if (root == nodes.end() or nodes.find(expr[1]) == nodes.end())
            return -1;
        else if (expr[1] == expr[0])
            return 1;

        root->second.val = 1.0;
        rim.push(&root->second);

        return bfs(rim, expr[1], nodes);
    }

    double bfs(queue<Variable100*> q, string until, map<string, Variable100> &nodes)
    {
        queue<Variable100*> rim;
        while (q.size() > 0)
        {
            Variable100 *me = q.front(); q.pop();
            me->visited = true;

            for (const auto &mulwith: me->mulwith)
            {
                map<string, Variable100>::iterator var = nodes.find(mulwith.first);

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
        map<string, Variable100> nodes;

        for (ulong x = 0; x < eqs.size(); x++)
        {
            if (eqs[x][0] == eqs[x][1]) continue;

            Variable100 *n, *d;
            map<string, Variable100>::iterator itn = nodes.find(eqs[x][0]);
            map<string, Variable100>::iterator itd = nodes.find(eqs[x][1]);
            if (itn != nodes.end())
                n = &itn->second;
            else n = new Variable100(eqs[x][0]);
            if (itd != nodes.end())
                d = &itd->second;
            else d = new Variable100(eqs[x][1]);

            n->addEdge(eqs[x][1], vals[x]);
            d->addEdge(eqs[x][0], 1.0 / vals[x]);

            nodes.insert(pair<string, Variable100>(n->name, *n));
            nodes.insert(pair<string, Variable100>(d->name, *d));
        }

        vector<double> rest;
        for (vector<string> q : queries)
        {
            map<string, Variable100>::iterator it = nodes.begin();
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

class Solution {
    //  ["a", "b" ...]
    map<string, int> names;
    // vector<int> variables;
    vector<bool> visited;

    /** [nominator, denominator] */
    vector<vector<double>> edges;

    int maxv;
public:
    vector<double> calcEquation(vector<vector<string>>& eqs, vector<double>& vals, vector<vector<string>>& queries) {
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
            else dId = names[n];
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
                edges[i][i] = 1.;
                this->visited[i] = false;
            }

            queue<int> root;
            root.push(names[qry[0]]);
            reslts.push_back(bfs(root, names[qry[1]]));
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
            bfs(q, until);
        return -1.;
    }
};

int main()
{
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

    return 0;
}
