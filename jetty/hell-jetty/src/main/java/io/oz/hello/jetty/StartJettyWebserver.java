package io.oz.hello.jetty;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletHandler;

public class StartJettyWebserver {

    public static void main(String[] args) throws Exception {
        Server server = new Server(8082);

        ServletHandler handler = new ServletHandler();
        server.setHandler(handler);

        handler.addServletWithMapping(ExampleServlet.class, "/*");
        server.start();
        server.join();

    }

}