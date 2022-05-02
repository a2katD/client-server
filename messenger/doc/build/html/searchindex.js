Search.setIndex({docnames:["client","common","index","logs","modules","server","unit_tests"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":5,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["client.rst","common.rst","index.rst","logs.rst","modules.rst","server.rst","unit_tests.rst"],objects:{"client.add_contact":[[0,0,1,"","AddContactDialog"]],"client.add_contact.AddContactDialog":[[0,1,1,"","possible_contacts_update"],[0,1,1,"","update_possible_contacts"]],"client.database":[[0,0,1,"","ClientDatabase"]],"client.database.ClientDatabase":[[0,0,1,"","Base"],[0,0,1,"","Contacts"],[0,0,1,"","KnownUsers"],[0,0,1,"","MessageHistory"],[0,1,1,"","add_contact"],[0,1,1,"","add_users"],[0,1,1,"","check_contact"],[0,1,1,"","check_user"],[0,1,1,"","contacts_clear"],[0,1,1,"","del_contact"],[0,1,1,"","get_contacts"],[0,1,1,"","get_history"],[0,1,1,"","get_users"],[0,1,1,"","save_message"]],"client.del_contact":[[0,0,1,"","DelContactDialog"]],"client.main_window":[[0,0,1,"","ClientMainWindow"]],"client.main_window.ClientMainWindow":[[0,1,1,"","add_contact"],[0,1,1,"","add_contact_action"],[0,1,1,"","add_contact_window"],[0,1,1,"","clients_list_update"],[0,1,1,"","connection_lost"],[0,1,1,"","delete_contact"],[0,1,1,"","delete_contact_window"],[0,1,1,"","edit_message"],[0,1,1,"","history_list_update"],[0,1,1,"","make_connection"],[0,1,1,"","message"],[0,1,1,"","select_active_user"],[0,1,1,"","send_message"],[0,1,1,"","set_active_user"],[0,1,1,"","set_disabled_input"],[0,1,1,"","sig_205"]],"client.start_dialog":[[0,0,1,"","UserNameDialog"]],"client.start_dialog.UserNameDialog":[[0,1,1,"","click"]],"client.transport":[[0,0,1,"","ClientTransport"]],"client.transport.ClientTransport":[[0,1,1,"","add_contact"],[0,1,1,"","connection_init"],[0,1,1,"","contacts_list_update"],[0,1,1,"","key_request"],[0,1,1,"","process_server_ans"],[0,1,1,"","remove_contact"],[0,1,1,"","run"],[0,1,1,"","send_message"],[0,1,1,"","transport_shutdown"],[0,1,1,"","user_list_update"]],"common.descriptrs":[[1,0,1,"","Port"]],"common.errors":[[1,0,1,"","IncorrectDataRecivedError"],[1,0,1,"","NonDictInputError"],[1,0,1,"","ReqFieldMissingError"],[1,0,1,"","ServerError"]],"common.log_decor":[[1,0,1,"","log"],[1,0,1,"","login_required"]],"common.metaclasses":[[1,0,1,"","ClientVerifier"],[1,0,1,"","ServerVerifier"]],"common.utils":[[1,2,1,"","get_message"],[1,2,1,"","send_message"]],"server.add_user":[[5,0,1,"","RegisterUser"]],"server.add_user.RegisterUser":[[5,1,1,"","save_data"]],"server.config_window":[[5,0,1,"","ConfigWindow"]],"server.config_window.ConfigWindow":[[5,1,1,"","initUI"],[5,1,1,"","open_file_dialog"],[5,1,1,"","save_server_config"]],"server.core":[[5,0,1,"","MessageProcessor"]],"server.core.MessageProcessor":[[5,1,1,"","autorize_user"],[5,1,1,"","init_socket"],[5,1,1,"","process_message"],[5,1,1,"","remove_client"],[5,1,1,"","run"],[5,1,1,"","service_update_lists"]],"server.main_window":[[5,0,1,"","MainWindow"]],"server.main_window.MainWindow":[[5,1,1,"","create_users_model"],[5,1,1,"","reg_user"],[5,1,1,"","rem_user"],[5,1,1,"","server_config"],[5,1,1,"","show_statistics"]],"server.remove_user":[[5,0,1,"","DelUserDialog"]],"server.remove_user.DelUserDialog":[[5,1,1,"","all_users_fill"],[5,1,1,"","remove_user"]],"server.stat_window":[[5,0,1,"","StatWindow"]],"server.stat_window.StatWindow":[[5,1,1,"","create_stat_model"],[5,1,1,"","initUI"]]},objnames:{"0":["py","class","Python \u043a\u043b\u0430\u0441\u0441"],"1":["py","method","Python \u043c\u0435\u0442\u043e\u0434"],"2":["py","attribute","Python \u0430\u0442\u0440\u0438\u0431\u0443\u0442"]},objtypes:{"0":"py:class","1":"py:method","2":"py:attribute"},terms:{"1":[0,5],"2":[0,5],"2048":0,"205":5,"3":[0,5],"4":0,"\u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446":[1,5],"\u0430\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430":1,"\u0430\u0434\u0440\u0435\u0441":[0,5],"\u0430\u043a\u0442\u0438\u0432\u043d":[0,5],"\u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c":0,"\u0430\u043b\u0444\u0430\u0432\u0438\u0442\u043d":2,"\u0430\u0440\u0433\u0435\u043c\u0435\u043d\u0442":5,"\u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442":[0,1],"\u0431\u0430\u0437":[0,5],"\u0431\u0434":0,"\u0431\u0435\u0437":5,"\u0432":[0,1,5],"\u0432\u0432\u0435\u0434\u0435\u043d":5,"\u0432\u0432\u043e\u0434":[0,5],"\u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432":0,"\u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430":0,"\u0432\u043e\u0437\u043c\u043e\u0436\u043d":0,"\u0432\u0441\u0435":5,"\u0432\u0441\u043f\u043e\u043c\u043e\u0433\u0430\u0442\u0435\u043b\u044c\u043d":1,"\u0432\u0445\u043e\u0434":0,"\u0432\u044b\u0431\u043e\u0440":[0,5],"\u0432\u044b\u0434\u0430":0,"\u0432\u044b\u0437\u043e\u0432":1,"\u0432\u044b\u043f\u043e\u043b\u043d\u044f":[0,1],"\u0432\u044b\u043f\u043e\u043d\u044f":1,"\u0432\u044b\u0445\u043e\u0434":0,"\u0433\u0435\u043d\u0435\u0440\u0438\u0440":[0,1],"\u0433\u043b\u0430\u0432\u043d":0,"\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a":5,"\u0434\u0430\u043d":[0,1,5],"\u0434\u0432\u043e\u0439\u043d":0,"\u0434\u0435\u043a\u0432\u0442\u0438\u0432\u0430\u0442\u043e\u0440":0,"\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440":1,"\u0434\u0435\u0441\u043a\u0440\u0438\u043f\u0442\u043e\u0440":1,"\u0434\u0438\u0430\u043b\u043e\u0433":[0,5],"\u0434\u043b\u0438\u043d":0,"\u0434\u043b\u044f":[0,1,5,6],"\u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d":0,"\u0434\u043e\u0431\u0430\u0432\u043b\u044f":0,"\u0435\u0433":5,"\u0435\u0441\u043b":[0,1,5],"\u0437\u0430":[0,1],"\u0437\u0430\u0432\u0435\u0440\u0448\u0430":0,"\u0437\u0430\u043a\u0440\u044b\u0442":0,"\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d":5,"\u0437\u0430\u043f\u043e\u043b\u043d\u044f":[0,5],"\u0437\u0430\u043f\u0440\u0430\u0448\u0438\u0432\u0430":0,"\u0437\u0430\u043f\u0440\u043e\u0441":1,"\u0437\u0430\u043f\u0443\u0441\u043a":5,"\u0437\u0430\u043f\u0443\u0441\u043a\u0430":0,"\u0437\u043d\u0430\u0447\u0435\u043d":1,"\u0438":[0,5],"\u0438\u0437":[0,5],"\u0438\u0437\u0432\u0435\u0441\u0442\u043d":0,"\u0438\u043b":0,"\u0438\u043c":0,"\u0438\u043c\u0435\u043d":0,"\u0438\u043d\u0438\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0442\u043e\u0440":5,"\u0438\u043d\u0438\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446":0,"\u0438\u0441\u043a\u043b\u044e\u0447\u0435\u043d":[0,1],"\u0438\u0441\u0442\u043e\u0440":0,"\u0438\u0449\u0435\u0442":5,"\u043a\u0430\u0447\u0435\u0441\u0442\u0432":5,"\u043a\u043b\u0430\u0441\u0441":[0,1,5],"\u043a\u043b\u0438\u0435\u043d\u0442":[0,1,3,5,6],"\u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a":[0,1],"\u043a\u043b\u044e\u0447":0,"\u043a\u043d\u043e\u043f\u043a":0,"\u043a\u043e\u043c\u0430\u043d\u0434":0,"\u043a\u043e\u043c\u0430\u043d\u0434\u043d":[0,5],"\u043a\u043e\u043c\u043c\u0430\u043d\u0434\u043d":0,"\u043a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u043d":1,"\u043a\u043e\u043d\u0442\u0430\u043a\u0442":[0,5],"\u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446":3,"\u043a\u043e\u043d\u0444\u0438\u0440\u0443\u0433\u0430\u0446":3,"\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d":0,"\u043a\u043e\u0440\u0442\u0435\u0436":0,"\u043a\u043e\u0442\u043e\u0440":[0,5],"\u043b\u0438\u0441\u0442":0,"\u043b\u043e\u0433\u0435\u0440":3,"\u043b\u043e\u0433\u0438\u043a":0,"\u043b\u043e\u0433\u0438\u0440\u043e\u0432\u0430\u043d":[1,3],"\u043c\u0435\u0441\u0435\u043d\u0434\u0436\u0435\u0440":1,"\u043c\u0435\u0441\u0441\u0435\u043d\u0434\u0436\u0435\u0440":5,"\u043c\u0435\u0442\u0430\u043a\u043b\u0430\u0441\u0441":1,"\u043c\u0435\u0442\u043e\u0434":[0,5],"\u043c\u043e\u0434\u0443\u043b":[0,1,2,3,6],"\u043d\u0430":[0,1,5],"\u043d\u0430\u043b\u0438\u0447":0,"\u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a":5,"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a":5,"\u043d\u0430\u0445\u043e\u0434":[0,1],"\u043d\u0435":[0,1],"\u043d\u0435\u0432\u0435\u0440\u043d":1,"\u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d":1,"\u043d\u0435\u0442":1,"\u043d\u0438\u0447":0,"\u043d\u043e\u0432":[0,5],"\u043d\u043e\u043c\u0435\u0440":0,"\u043e":0,"\u043e\u0431":0,"\u043e\u0431\u043c":0,"\u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d":0,"\u043e\u0431\u043d\u043e\u0432\u043b\u044f":0,"\u043e\u0431\u043e\u043b\u043e\u0447\u043a":5,"\u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430":[0,5],"\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a":[0,5],"\u043e\u0431\u044a\u0435\u043a\u0442":1,"\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d":1,"\u043e\u043a":0,"\u043e\u043a\u043d":[0,5],"\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d":0,"\u043e\u0441\u043d\u043e\u0432\u043d":[0,5],"\u043e\u0442":[0,1,5],"\u043e\u0442\u0432\u0435\u0447\u0430":0,"\u043e\u0442\u0434\u0435\u043b\u044c\u043d":5,"\u043e\u0442\u043a\u0440\u044b\u0442":5,"\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d":0,"\u043e\u0442\u043f\u0440\u0430\u0432\u043a":[0,5],"\u043e\u0442\u043f\u0440\u0430\u0432\u043b\u044f":0,"\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432":1,"\u043e\u0447\u0438\u0449\u0430":0,"\u043e\u0448\u0438\u0431\u043a":[0,1],"\u043f\u0430\u043a\u0435\u0442":5,"\u043f\u0430\u043f\u043a":5,"\u043f\u0430\u0440\u043e\u043b":0,"\u043f\u0430\u0440\u0441\u0435\u0440":0,"\u043f\u0435\u0440\u0435\u0434\u0430\u0432\u0430":1,"\u043f\u0435\u0440\u0435\u0434\u0430\u0447":1,"\u043f\u043e":0,"\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430":0,"\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d":0,"\u043f\u043e\u0438\u0441\u043a":2,"\u043f\u043e\u043b":[0,1],"\u043f\u043e\u043b\u043e\u0442\u043a":0,"\u043f\u043e\u043b\u0443\u0447":1,"\u043f\u043e\u043b\u0443\u0447\u0430":0,"\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b":[0,5],"\u043f\u043e\u043c\u043e\u0449":0,"\u043f\u043e\u0440\u0442":[0,1,5],"\u043f\u043e\u0441\u0442\u0443\u043f\u0430":5,"\u043f\u043e\u0442\u0435\u0440":0,"\u043f\u043e\u0442\u043e\u043a":5,"\u043f\u043e\u044d\u0442":0,"\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d":5,"\u043f\u0440\u0435\u0440\u0432\u0430":5,"\u043f\u0440\u0438":0,"\u043f\u0440\u0438\u0435\u043c":0,"\u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d":0,"\u043f\u0440\u0438\u043d\u0438\u043c\u0430":[0,5],"\u043f\u0440\u0438\u043d\u044f\u0442":1,"\u043f\u0440\u043e\u0432\u0435\u0440\u043a":[0,1,5],"\u043f\u0440\u043e\u0432\u0435\u0440\u044f":[0,1,5],"\u043f\u0440\u043e\u0435\u043a\u0442":[1,3],"\u043f\u0440\u043e\u0438\u0437\u043e\u0439\u0434\u0435\u0442":0,"\u043f\u0443\u0431\u043b\u0438\u0447\u043d":0,"\u043f\u0443\u0441\u0442":0,"\u0440\u0430\u0431\u043e\u0442":0,"\u0440\u0430\u0431\u043e\u0442\u0430":5,"\u0440\u0435\u0430\u043b\u0438\u0437":5,"\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446":5,"\u0441":[0,3,5,6],"\u0441\u0432\u044f\u0437":5,"\u0441\u0435\u0440\u0432\u0435\u0440":[0,1,3,5,6],"\u0441\u0435\u0440\u0432\u0435\u0440\u043d":1,"\u0441\u0435\u0440\u0432\u0438\u0441\u043d":5,"\u0441\u0435\u0442":0,"\u0441\u0438\u0433\u043d\u0430\u043b":0,"\u0441\u0438\u0441\u0442":0,"\u0441\u043b\u043e\u0432\u0430\u0440":[1,5],"\u0441\u043b\u043e\u0442":0,"\u0441\u043c\u0430\u0439\u043b\u0438\u043a":0,"\u0441\u043e":[0,5],"\u0441\u043e\u0431\u0435\u0441\u0435\u0434\u043d\u0438\u043a":0,"\u0441\u043e\u0434\u0435\u0440\u0436":[0,1],"\u0441\u043e\u0434\u0435\u0440\u0436\u0430":0,"\u0441\u043e\u0434\u0438\u043d\u0435\u043d":5,"\u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d":[0,5],"\u0441\u043e\u0437\u0434\u0430":5,"\u0441\u043e\u043a\u0435\u0442":[1,5],"\u0441\u043e\u043e\u0431\u0449\u0430":0,"\u0441\u043e\u043e\u0431\u0449\u0435\u043d":[0,5],"\u0441\u043e\u0441\u0442\u0430":2,"\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d":5,"\u0441\u043e\u0445\u0440\u0430\u043d\u044f":[0,5],"\u0441\u043f\u0438\u0441\u043a":[0,1,5],"\u0441\u043f\u0438\u0441\u043e\u043a":[0,5],"\u0441\u0442\u0430\u0432":0,"\u0441\u0442\u0430\u0440\u0442\u043e\u0432":0,"\u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a":5,"\u0441\u0442\u043e\u0440\u043e\u043a":5,"\u0441\u0442\u0440\u043e\u043a":0,"\u0442\u0430\u0431\u043b\u0438\u0446":[0,5],"\u0442\u0435\u0441\u0442":6,"\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d":0,"\u0442\u043e\u043b\u044c\u043a":[0,5],"\u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442":0,"\u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d":0,"\u0443\u0434\u0430\u043b\u0435\u043d":[0,5],"\u0443\u0434\u0430\u043b\u044f":5,"\u0443\u0436":0,"\u0443\u043a\u0430\u0437\u0430\u0442\u0435\u043b":2,"\u0443\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430":0,"\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a":0,"\u0443\u0442\u0438\u043b":6,"\u0444\u0430\u0439\u043b":[1,3,5,6],"\u0444\u043b\u0430\u0433":0,"\u0444\u0443\u043d\u043a\u0446":[0,1,5],"\u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430":0,"\u0446\u0438\u043a\u043b":[0,5],"\u0447\u0442\u043e":1,"\u0448\u0438\u0444\u0440":0,"\u0449\u0435\u043b\u0447\u043a":0,"\u044d\u043b\u0435\u043c\u0435\u043d\u0442":0,"\u044e\u043d":6,"class":[0,1,5],"new":0,"package":4,a:[0,5],accepts:0,add_contact:[2,4],add_contact_action:0,add_contact_window:0,add_user:[2,4],add_users:0,addcontactdialog:0,alias:1,all_users_fill:5,and:0,any:0,arg_parser:0,arguments:0,attributes:0,autorize_user:5,base:0,bases:1,be:0,bit:0,called:0,cannot:0,check_contact:0,check_user:0,click:0,client:[2,4,5],clientdatabase:0,clientmainwindow:0,clients_list_update:0,clienttransport:0,clientverifier:1,clsdict:1,clsname:1,common:[2,4],config:5,config_client_log:[2,4],config_server_log:[2,4],config_window:[2,4],configwindow:5,connection_init:0,connection_lost:0,contact:0,contacts:0,contacts_clear:0,contacts_list_update:0,contents:4,core:[2,4],create_stat_model:5,create_users_model:5,database:[2,4],del_contact:[2,4],delcontactdialog:0,delete_contact:0,delete_contact_window:0,deluserdialog:5,descriptrs:[2,4],direction:0,edit_message:0,errors:[2,4],featureless:0,func:1,get_contacts:0,get_history:0,get_message:1,get_users:0,given:0,has:0,hierarchy:0,history_list_update:0,icq:5,incorrectdatarecivederror:1,ini:5,init_socket:5,initui:5,instance:0,ip:0,ip_address:0,it:0,item:0,key_request:0,keys:0,knownusers:0,kwargs:0,launcher:4,launcher_ubuntu:4,listen_address:5,listen_port:5,locals:1,log:1,log_decor:[2,4],login_required:1,logs:[2,4],main_window:[2,4],main_window_conv:4,mainwindow:5,make_connection:0,message:[0,5],messagehistory:0,messageprocessor:5,messenger:[],metaclasses:[2,4],missing_field:1,module:[2,4],n:0,name:0,new_contact:0,no:0,no_gui:5,nondictinputerror:1,of:[0,1],open_file_dialog:5,p:[0,5],passwd:0,password:0,port:[0,1],possible_contacts_update:0,process_message:5,process_server_ans:0,py:2,reg_user:5,registeruser:5,rem_user:5,remove_client:5,remove_contact:0,remove_user:[2,4],reqfieldmissingerror:1,returns:0,rsa:0,run:[0,5],save_data:5,save_message:0,save_server_config:5,select_active_user:0,send_message:[0,1],server:[2,4],server_config:5,server_database:4,servererror:1,serververifier:1,service_update_lists:5,set_active_user:0,set_disabled_input:0,show_statistics:5,sig_205:0,smile:0,sock:5,sqlite:0,start_dialog:[2,4],stat_window:[2,4],statwindow:5,submodules:4,subpackages:4,test_client:[2,4],test_server:[2,4],test_utils:4,text:1,that:0,the:0,to:0,trans_obj:0,transport:[2,4],transport_shutdown:0,typeerror:1,unit_test:2,unit_tests:4,update_possible_contacts:0,user:0,user_list_update:0,username:0,usernamedialog:0,users_list:0,utils:[2,4],variables:[2,4],when:0,wrap:1},titles:["Client module","Common module","Welcome to ICQ\u2019s documentation!","logs module","messenger","Server module","unit_test module"],titleterms:{"package":[],add_contact:0,add_user:5,and:2,client:0,common:1,config_client_log:3,config_server_log:3,config_window:5,contents:2,core:5,database:[0,5],del_contact:0,descriptrs:1,documentation:2,errors:1,icq:2,indices:2,launcher:[],launcher_ubuntu:[],log_decor:1,logs:3,main_window:[0,5],main_window_conv:[],messenger:4,metaclasses:1,module:[0,1,3,5,6],py:[0,1,3,5,6],remove_user:5,s:2,server:5,server_database:[],start_dialog:0,stat_window:5,submodules:[],subpackages:[],tables:2,test_client:6,test_server:6,test_utils:[],to:2,transport:0,unit_test:6,unit_tests:[],utils:1,variables:1,welcome:2}})