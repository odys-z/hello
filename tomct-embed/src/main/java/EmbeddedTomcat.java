import java.io.File;
import java.io.InputStream;
import java.net.URL;
import org.apache.catalina.connector.Connector;
import org.apache.catalina.Context;
import org.apache.catalina.Engine;
import org.apache.catalina.Host;
import org.apache.catalina.ant.DeployTask;
import org.apache.catalina.startup.CatalinaProperties;
import org.apache.catalina.startup.Tomcat;
import org.apache.coyote.http11.Http11NioProtocol;
import org.apache.tomcat.util.buf.ByteChunk;
import org.apache.catalina.Container;

public class EmbeddedTomcat {

  private String path = null;
  private Tomcat embedded = null;
  private Host host = null;
  /**
    * Default Constructor
    *
    */
  public EmbeddedTomcat() {

  }

  /**
    * Basic Accessor setting the value of the context path
    *
    * @param path - the path
    */
  public void setPath(String path) {

    this.path = path;
  }

  /**
    * Basic Accessor returning the value of the context path
    *
    * @return - the context path
    */
  public String getPath() {

    return path;
  }

  /**
    * This method Starts the Tomcat server.
    */
  public void startTomcat() throws Exception {

      // Tomcat tomcat = getTomcatInstance();

	  Tomcat tomcat = setUp();
	  
      // No file system docBase required
      Context ctx = tomcat.addContext("", null);

      Tomcat.addServlet(ctx, "myServlet", new HelloWorld());
      ctx.addServletMappingDecoded("/", "myServlet");

      tomcat.start();

      // ByteChunk res = getUrl("http://localhost:8080/");
      // Assert.assertEquals("Hello world", res.toString());
  }
  
  public Tomcat setUp() throws Exception {

      // Trigger loading of catalina.properties
      CatalinaProperties.getProperty("foo");

      File appBase = new File("webapps");
      if (!appBase.exists() && !appBase.mkdir()) {
          throw new Exception("Unable to create appBase for test");
      }

      Tomcat tomcat = new Tomcat();

//      String protocol = getProtocol();
//      Connector connector = new Connector(protocol);
      Connector connector = new Connector(Http11NioProtocol.class.getName());
      
      // Listen only on localhost
      // Assert.assertTrue(connector.setProperty("address", InetAddress.getByName("localhost").getHostAddress()));

      // Use random free port
      connector.setPort(0);
      // By default, a connector failure means a failed test
      connector.setThrowOnFailure(true);
      // Mainly set to reduce timeouts during async tests
      // Assert.assertTrue(connector.setProperty("connectionTimeout", "3000"));

      tomcat.getService().addConnector(connector);
      tomcat.setConnector(connector);

      File catalinaBase = new File(".");
      tomcat.setBaseDir(catalinaBase.getAbsolutePath());
      tomcat.getHost().setAppBase(appBase.getAbsolutePath());

//      accessLogEnabled = Boolean.parseBoolean(
//          System.getProperty("tomcat.test.accesslog", "false"));
//      if (accessLogEnabled) {
//          String accessLogDirectory = System
//                  .getProperty("tomcat.test.reports");
//          if (accessLogDirectory == null) {
//              accessLogDirectory = new File(getBuildDirectory(), "logs")
//                      .toString();
//          }
//          AccessLogValve alv = new AccessLogValve();
//          alv.setDirectory(accessLogDirectory);
//          alv.setPattern("%h %l %u %t \"%r\" %s %b %I %D");
//          tomcat.getHost().getPipeline().addValve(alv);
//      }

      // Cannot delete the whole tempDir, because logs are there,
      // but delete known subdirectories of it.
//      addDeleteOnTearDown(new File(catalinaBase, "webapps"));
//      addDeleteOnTearDown(new File(catalinaBase, "work"));
      
      return tomcat;
  }


  /**
    * This method Stops the Tomcat server.
    */
  public void stopTomcat() throws Exception {
    // Stop the embedded server
    embedded.stop();
  }

  /**
    * Registers a WAR with the container.
    *
    * @param contextPath - the context path under which the
    *               application will be registered
    * @param warFile - the URL of the WAR to be
    * registered.
    */
  public void registerWAR(String contextPath, URL warFile)
    throws Exception {

    if ( contextPath == null ) {

      throw new Exception("Invalid Path : " + contextPath);
    }
    if( contextPath.equals("/") ) {

      contextPath = "";
    }
    if ( warFile == null ) {

      throw new Exception("Invalid WAR : " + warFile);
    }

//    Deployer deployer = (Deployer)host;
//    Context context = deployer.findDeployedApp(contextPath);
//
//    if (context != null) {
//
//      throw new
//        Exception("Context " + contextPath
//        + " Already Exists!");
//    }
//    deployer.install(contextPath, warFile);
    
    DeployTask deployTask = new DeployTask() {

        @Override
        public void execute(String command, InputStream istream, String contentType, long contentLength)
                throws BuildException {
            // Assert.assertEquals("/deploy?path=somepath", command);
            // Assert.assertEquals("application/octet-stream", contentType);
            try {
                istream.close();
            } catch (IOException e) {
            }
        }
    };
  }

  /**
    * Unregisters a WAR from the web server.
    *
    * @param contextPath - the context path to be removed
    */
  public void unregisterWAR(String contextPath)
    throws   Exception {

    Context context = host.map(contextPath);
    if ( context != null ) {

      embedded.removeContext(context);
    }
    else {

      throw new
        Exception("Context does not exist for named path : "
        + contextPath);
    }
  }

  public static void main(String args[]) {

    try {

      EmbeddedTomcat tomcat = new EmbeddedTomcat();
      tomcat.setPath("d:/jakarta-tomcat-4.0.1");
      tomcat.startTomcat();

      URL url =
        new URL("file:D:/jakarta-tomcat-4.0.1"
        + "/webapps/onjava");
      tomcat.registerWAR("/onjava", url);

      Thread.sleep(1000000);

      tomcat.stopTomcat();

      System.exit(0);
    }
    catch( Exception e ) {

      e.printStackTrace();
    }
  }
}