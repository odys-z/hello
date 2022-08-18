package io.oz.hello.jetty;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Not directly possible:
 * 
 * https://stackoverflow.com/a/13955415/7362888
 * 
 * @author ody
 */
@WebServlet( asyncSupported = false, urlPatterns={"/anno/*"})
public class AnnotateServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("application/json");
        response.setStatus(HttpServletResponse.SC_OK);
        response.getWriter().println("{ \"status\": \"Annotated\"}");
    }
}