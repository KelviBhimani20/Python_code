<%@ page import="java.sql.*" %>
<%@ include file="connection.jsp" %>

<%
    int id = Integer.parseInt(request.getParameter("id"));

    String sql = "DELETE FROM student WHERE id = ?";

    PreparedStatement ps = connection.prepareStatement(sql);

    ps.setInt(1, id);

    ps.executeUpdate();

    ps.close();
    connection.close();

    response.sendRedirect("index.jsp");
%>