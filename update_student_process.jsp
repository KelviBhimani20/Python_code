<%@ page import="java.sql.*" %>
<%@ include file="connection.jsp" %>

<%
    request.setCharacterEncoding("UTF-8");

    int id = Integer.parseInt(request.getParameter("id"));
    String name = request.getParameter("name");
    String course = request.getParameter("course");
    int semester = Integer.parseInt(request.getParameter("semester"));
    String division = request.getParameter("division");

    String sql = "UPDATE student SET name=?, course=?, semester=?, division=? WHERE id=?";

    PreparedStatement ps = connection.prepareStatement(sql);

    ps.setString(1, name);
    ps.setString(2, course);
    ps.setInt(3, semester);
    ps.setString(4, division);
    ps.setInt(5, id);

    ps.executeUpdate();

    ps.close();
    connection.close();

    response.sendRedirect("index.jsp");
%>  