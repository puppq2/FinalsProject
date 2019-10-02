{% extends "layout.html" %}

{% block content %}
<div id="mySidenav" class="sidenav">
  <a href="{{ url_for('admin') }}"><h1>Home</h1></a>
  <a href="{{ url_for('employee') }}">Employee</a>
  <a href="{{ url_for('item') }}">Items</a>
  <a href="#">Sales</a>
  <a href="#">Inventory</a>
  <a href="{{ url_for('supplier') }}">Supplier</a>
  <a href="#">Delivery</a>
</div>
<div class="main">
  <center>
 <h1>Employee</h1>
  </center>
  {{ form.search.label }}{{ form.search }}
</div>

            <div class="container">
 <div class="alert alert-success">
             <p><strong>Today is:</strong></p>
                        <i class="icon-calendar icon-large"></i>
                        <?php
                        date_default_timezone_set("Asia/Manila");
                      //  $Today = date('d:m:y');
                      //  $new = date('l, F d, Y', strtotime($Today));
                       //  echo $new;
                       echo "<span style='color:red;font-weight:bold;'>Date: </span>". date('F j, Y ');
                        ?>
						 </div>
<table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered" id="example">
                        <div class="alert alert-info">
                            <button type="button" class="close" data-dismiss="alert">&times;</button>
                            <strong><i class="icon-user icon-large"></i>&nbsp;MANAGE EMPLOYEE'S</strong>
                        </div>
                        <thead>
                            <tr>
                                <th style="text-align:center;">FirstName</th>
                                <th style="text-align:center;">MiddleName</th>
                                <th style="text-align:center;">LastName</th>
                                <th style="text-align:center;">Email</th>
                                <th style="text-align:center;">Address</th>
                                <th style="text-align:center;">Username</th>
                                <th style="text-align:center;">Password</th>
                                <th style="text-align:center;">Action</th>

                            </tr>
                        </thead>
                        <tbody>

            <tr>

            <td style="text-align:center; word-break:break-all; width:300px;"> <?php echo $row ['fname']; ?></td>
            <td style="text-align:center; word-break:break-all; width:200px;"> <?php echo $row ['mname']; ?></td>
            <td style="text-align:center; word-break:break-all; width:200px;"> <?php echo $row ['lname']; ?></td>
            <td style="text-align:center; word-break:break-all; width:500px;"> <?php echo $row ['email']; ?></td>
            <td style="text-align:center; word-break:break-all; width:500px;"> <?php echo $row ['address']; ?></td>
            <td style="text-align:center; word-break:break-all; width:200px;"> <?php echo $row ['username']; ?></td>
            <td style="text-align:center; word-break:break-all; width:200px;"> <?php echo $row ['password']; ?></td>

            <td style="text-align:center; width:800px;">
              <a href="edit.php<?php echo '?id='.$id; ?>" class="btn btn-info">Edit</a>
               <a href="{{ url_for('admin') }}"  data-toggle="modal"  class="btn btn-danger" >Delete </a>
            </td>

                <!-- Modal -->
            <div id="delete<?php  echo $id;?>" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
            <div class="modal-header">
            <h3 id="myModalLabel">Delete</h3>
            </div>
            <div class="modal-body">
            <p><div class="alert alert-danger">Are you Sure you want Delete?</p>
            </div>
            <hr>
            <div class="modal-footer">
            <button class="btn btn-inverse" data-dismiss="modal" aria-hidden="true">No</button>
            <a href="delete.php<?php echo '?id='.$id; ?>" class="btn btn-danger">Yes</a>
            </div>
            </div>
            </div>
            </tr>

            <!-- Modal Bigger Image -->
            <div id="<?php  echo $id;?>" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
            <div class="modal-header">

            <h3 id="myModalLabel"><b><?php echo $row['fname']." ".$row['lname']; ?></b></h3>
            </div>
            <div class="modal-body">
            <?php if($row['location'] != ""): ?>
            <img src="upload/<?php echo $row['location']; ?>" style="width:390px; border-radius:9px; border:5px solid #d0d0d0; margin-left: 63px; height:387px;">
            <?php else: ?>
            <img src="images/default.png" style="width:390px; border-radius:9px; border:5px solid #d0d0d0; margin-left: 63px; height:387px;">
            <?php endif; ?>
            </div>
            <div class="modal-footer">
            <button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
            </div>
            </div>

            <?php } ?>
                        </tbody>
                    </table>
{{myUser}}

{% endblock content %}
