<%@ page import="java.sql.*" %>
<%@ include file="connection.jsp" %>

<%
    int id = Integer.parseInt(
        request.getParameter("id")
    );

    String sql = "SELECT * FROM student WHERE id = ?";

    PreparedStatement ps =
        connection.prepareStatement(sql);

    ps.setInt(1, id);

    ResultSet rs = ps.executeQuery();

    if (rs.next()) {
        String name = rs.getString("name");
        String course = rs.getString("course");
        int semester = rs.getInt("semester");
        String division = rs.getString("division");
%>

<form action="update_student_process.jsp" method="post">

    <input type="hidden" name="id" value="<%= id %>"/>

    <input type="text" name="name"
           value="<%= name %>" placeholder="Enter Name"/>

    <input type="text" name="course"
           value="<%= course %>" placeholder="Enter Course"/>

    <input type="number" name="semester"
           value="<%= semester %>" placeholder="Enter Semester"/>

    <input type="text" name="division"
           value="<%= division %>" placeholder="Enter Division"/>

    <input type="submit" value="Update Student"/>

</form>

<%
    } else {
        out.println("Student not found.");
    }

    rs.close();
    ps.close();
    connection.close();
%>