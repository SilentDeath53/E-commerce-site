@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Define other admin routes for managing products, orders, customers, etc.
