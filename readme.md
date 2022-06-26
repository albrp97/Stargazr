# Alberto Rodero for Stargazr Challenges

# Challenge 1:

We recently had a water leak, so we decided to investigate it a bit. We know the water pressure at the ground floor, which decreases by 1 each level you go up. At some floor, the water pipe has broken and it's flowing freely at that pressure. It also leaks to the levels below, and we know that each floor the water leaks, it does at less pressure. Given the report of the leak, we want you to tell us the floor where it started.

Input

The first line is the number of cases C, and C cases follow. Each case is a line with 4 integers P, F, G, I. P is the pressure of the leak, F is the floor where the leak was reported (having 0 as ground floor), G is the ground floor pressure and I is the insulation of the building. An insulation of I means that every level the leak goes down, its pressure is decreased by I.

Output

For each case, there should be a line starting with Case #c: followed by the floor where the leak started

Execution:

Applied mathematical formula to each case. Since cases are independent from eachother it can be optimized by running it parallel in a cluster, but since the dataset is not too big i didn't find it necessary

# Callenge 2:

Last year, we designed a service that syncs all the computers of the company to share files, but we disabled it because it was a bit buggy. However, yesterday it triggered without notice and our network got flooded with requests.

We have gathered the network logs of all our computers, which never communicate between them unless the DDOS service is running. Can you help us discover which computer initiated the attack?

Input

The input for this problem is a zip file with the logs of each computer, named with their IPs. Each row of the log represents a request sorted by moment in ascending order. Incoming requests start with IN and outgoing requests start with OUT.

Output

A text file with the IP of the computer that started the attack.

Execution:

These computers only connect in local network when attacked, so we have to look for the first one to communicate in the local network

Starting from a random computer in the network (i2) we jump between first IN connections until we always arrive to 172.16.41.255 which is the first one to communicate, thus this is the one to initiate the attack

# Challenge 3:

Some months ago we started the Stargazr newspaper. To motivate people to write, we started a pay-by-the-word system. However, most of our articles contain code, so we came up with a way to compute how code is paid.

We pay our writers depending on the expressions, according to this table:

Description	

Samples

$7	Name
$5	Operator
$4	Grouping
$3	Number
$2	String
$0	Blank

We only pay for the valid formulas, which are expressions made of the previous parts and only contain ASCII characters. Your task here is to help us automate this tedious problem.

Limits
The small input contains 80 formulas.
Every line has 500 characters at most.
Input
The first line is the number of cases C, and C cases follow. Then, every other line is a formula (formulas don't contain line breaks).

Output
For each case, there should be a line starting with Case #c: followed by the amount we should pay for it without units.

Execution:

Following a compiler's approach it checks individual tokens and depending on kind it divides them into blocks. For example a String is a block but an operator isn't. Sum of price is blocks plus individual tokens. If there's any error the value is 0.

Since this is not a real compilator expresions such as +++++++ are valid even though they serve no purpose. Expresions like ++++ are considered multiple operators. 

Although i followed the challenge like i was building a compiler i did not implement appropiate classes or methods due to the simplicity of the challenge.