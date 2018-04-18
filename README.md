# PlagiarismCheck
Python script that uses FAROO Web Search API to detect plagiarism<br/>
Register for FAROO API key <a href="http://www.faroo.com/hp/api/api.html">here</a> <br/>
The script works as follows -<br/>
<ul>
	<li>The script divides the document into n words subtrings. </li><br/>
	<li>Each substring are sent to FAROO Web Search API as a query.</li><br/>
	<li>Plagiarism is checked into returned result from Faroo.</li><br/>
	<li>The final plagiarism % is calculated using the formula - </li><br/>
	<li><code>(no of plagiarized subs/ total no of subs)*100</code></li>
</ul>