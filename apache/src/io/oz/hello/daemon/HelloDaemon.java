package io.oz.hello.daemon;

public class HelloDaemon {
	   /**
	    * Single static instance of the service class
	    */
	   private static HelloDaemon 
	       serviceInstance = new HelloDaemon();
		
	   /**
	    * Static method called by prunsrv to start/stop
	    * the service.  Pass the argument "start"
	    * to start the service, and pass "stop" to
	    * stop the service.
	    */
	   public static void windowsService(String args[]) {
	      String cmd = "start";
	      if(args.length > 0) {
	         cmd = args[0];
	      }
		
	      if("start".equals(cmd)) {
	         serviceInstance.start();
	      }
	      else {
	         serviceInstance.stop();
	      }
	   }

	   /**
	    * Flag to know if this service
	    * instance has been stopped.
	    */
	   private boolean stopped = false;
		
		
	   /**
	    * Start this service instance
	    */
	   public void start() {
		
	      stopped = false;
			
	      System.out.println("My Service Started "
	                         + new java.util.Date());
			
	      while(!stopped) {
	         System.out.println("My Service Executing "
	                             + new java.util.Date());
	         synchronized(this) {
	            try {
	               this.wait(10000);
	            }
	            catch(InterruptedException ie){}
	         }
	      }
			
	      System.out.println("My Service Finished "
	                          + new java.util.Date());
	   }
		
	   /**
	    * Stop this service instance
	    */
	   public void stop() {
	      stopped = true;
	      synchronized(this) {
	         this.notify();
	      }
	   }
}