using Renci.SshNet;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConnectSSH
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 4)
            {
                Console.WriteLine("Connecting . . .");
                bool retry_status = true;
                int retry_time = 0;
                do
                {
                    try
                    {
                        retry_time += 1;
                        Console.WriteLine(string.Format("Reconnecting ({0}) . . .", retry_time));
                        SshClient _client = new SshClient(args[0], int.Parse(args[1]), args[2], args[3]);
                        _client.ConnectionInfo.Timeout = TimeSpan.FromSeconds(7200);
                        _client.Connect();
                        Console.WriteLine("Port forwarding . . .");
                        ForwardedPortDynamic port = new ForwardedPortDynamic("127.0.0.1", 1080);
                        _client.AddForwardedPort(port);
                        if (_client.IsConnected)
                        {
                            port.Start();
                        }
                        Console.WriteLine("Connected!");
                        retry_status = false;
                    }
                    catch (Exception)
                    {
                        retry_status = true;
                    }
                    
                } while (retry_status == true);
            }
            else
            {
                Console.WriteLine("Missing parameter.");
               
            }
            Console.ReadLine();
        }
    }
}
