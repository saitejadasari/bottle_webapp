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
    <td>{{str(item['desc'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/delete/{{str(item['id'])}}">x</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">New Item...</a>
</body>
</html>