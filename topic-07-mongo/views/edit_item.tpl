<html>
<body>
    Edit this Item...
    <hr/>
    <form action="/edit/{{topic}}/{{id}}" method="post">
        <p>Edit Item:<input name="description" value="{{description}}"/></p>
        <p><button type="submit">Submit</button></p>
    </form>
    <hr/>
    <a href="/list">Cancel</a>
</body>
</html>