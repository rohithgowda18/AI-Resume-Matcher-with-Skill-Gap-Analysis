monitor->CheckForLostPackets ();
Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier> (flowmon.GetClassifier ());
std::map<FlowId, FlowMonitor::FlowStats> stats = monitor->GetFlowStats ();
for (std::map<FlowId, FlowMonitor::FlowStats>::const_iterator iter = stats.begin (); iter != stats.end
(); ++iter)
{
Ipv4FlowClassifier::FiveTuple t = classifier->FindFlow (iter->first);
NS_LOG_UNCOND("Flow ID: " << iter->first << " Src Addr " << t.sourceAddress << " Dst Addr " <<
t.destinationAddress);
NS_LOG_UNCOND("Tx Packets = " << iter->second.txPackets);
NS_LOG_UNCOND("Rx Packets = " << iter->second.rxPackets);
NS_LOG_UNCOND("lostPackets Packets = " << iter->second.lostPackets);
NS_LOG_UNCOND("Throughput: " << iter->second.rxBytes * 8.0 / (iter-
>second.timeLastRxPacket.GetSeconds()-iter->second.timeFirstTxPacket.GetSeconds()) / 1024 << "
Kbps");
NS_LOG_UNCOND("----------------------" );
}


import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws Exception {
        try (Socket sock = new Socket("127.0.0.1", 4000);
             BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
             PrintWriter pwrite = new PrintWriter(sock.getOutputStream(), true);
             BufferedReader socketRead = new BufferedReader(new InputStreamReader(sock.getInputStream()))) {
            
            System.out.println("Enter the filename:");
            String fname = keyRead.readLine();
            pwrite.println(fname);

            String str;
            while ((str = socketRead.readLine()) != null) {
                System.out.println(str);
            }
        }
    }
}


import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(4000);
        System.out.println("Server started. Waiting for client...");
        
        try {
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected");
                
                try (BufferedReader socketRead = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                     PrintWriter pwrite = new PrintWriter(clientSocket.getOutputStream(), true)) {
                    
                    String fname = socketRead.readLine();
                    
                    try (BufferedReader fileRead = new BufferedReader(new FileReader(fname))) {
                        String str;
                        while ((str = fileRead.readLine()) != null) {
                            pwrite.println(str);
                        }
                    } catch (FileNotFoundException e) {
                        pwrite.println("File not found: " + fname);
                    }
                } finally {
                    clientSocket.close();
                }
            }
        } finally {
            serverSocket.close();
        }
    }
}
