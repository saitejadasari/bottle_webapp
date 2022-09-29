<html>
<body>
<h1>Shopping List</h1>
<hr/>
<table>
%count = 1
% for item in shopping_list:
  <tr>
    <td>{{str(count)}}</td>
    % count += 1
    <td>{{str(item['description'])}}</td>
    <td>{{str(item['quantity'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/delete/{{str(item['id'])}}">x</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/add" method="post">
    <p>Enter New item <input name="description"/></p>
    <p>Enter Quantity <input name="quantity"/></p>
    <p><button type="submit">Submit</button></p>
</form>
</body>
</html>