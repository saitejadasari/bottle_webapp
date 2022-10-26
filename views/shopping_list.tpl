<html>
<body>
%topic_id = int(topic) if topic else 2
%topic_name = "Direct SQL"
<h1>Shopping List</h1>
<%
print("Topic in template", topic_id)
    if topic_id == 1 or topic_id == 2:
        topic_name = "Direct SQL"
    elif topic_id == 3:
        topic_name = "Dataset"
    else:
        topic_name = "Peewee"
    end
%>
<h3>Topic - using {{topic_name}}</h3>
<hr/>

<table>
%count = 1
<tr>
    <th>S.No</th>
    <th>Item</th>
    <th>Quantity</th>
</tr>

% for item in shopping_list:
    <tr>
        <td>{{str(count)}}</td>
        % count += 1
        <td>{{str(item['description'])}}</td>
        <td>{{str(item.get('quantity', 1))}}</td>
        <td><a href="/edit/{{topic_id}}/{{str(item['id'])}}">edit</a></td>
        <td><a href="/delete/{{topic_id}}/{{str(item['id'])}}">x</a></td>
    </tr>
% end
</table>
<hr/>
<form action="/{{topic_id}}/add" method="post">
    <p>Enter New item <input name="description"/></p>
    <p>Enter Quantity <input name="quantity"/></p>
    <p><button type="submit">Submit</button></p>
</form>

<p display='inline'>
<p>Topics</p>
<a href="/2/redirect">Direct SQL</a>
<a href="/4/redirect">Peewee</a>
<a href="/3/redirect">Dataset</a>
</p>
</body>
</html>