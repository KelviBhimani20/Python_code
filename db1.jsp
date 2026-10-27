
<%@ page import="java.sql.*" %>
<%
Connection connection = null;

try {
    Class.forName("com.mysql.cj.jdbc.Driver");

    connection = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/db1",
        "root",
        ""
    );

} catch (Exception e) {
    out.println("DATABASE ERROR: " + e.getMessage());
}
%>
